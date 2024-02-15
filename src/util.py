from src.vector import Vector2D, np
from src.constants import Constants as c


class Util:

    def __init__(self):
        self.speedValuesStraight = (40, 50, 40)
        self.speedValuesCurve = (40, 40, 40)

    def convert_cords(self, cords, map) -> list:
        """ 
        Converts pixel coordinates
        (0, 0) is bottom left, scaling to cm applied

        Params:
        cords: list[int, int] - pixel coordinates
        map: Map - map object
        """
        
        return cords[0] * map.X_SCALE, (c.SCREEN_HEIGHT - cords[1]) * map.Y_SCALE
    

    def angleBetweenVectors(self, v1: Vector2D, v2: Vector2D) -> float:
        """ 
        Calculates turning angle using vector angles
        Checks if y-Cord of v2 is over/under/on v1 based on dir 
        """
        
        angle = np.degrees(np.arccos(np.clip(np.dot(v1.get_unitVector(), v2.get_unitVector()), -1.0, 1.0)))
        invert = (-1 if 2 <= v1.dir <= 4 else 1)
        
        # If v1 is vertical
        if v1.dir == 1: 
            return (-angle if v2.values[1][0] < v1.values[1][0] else angle) 
        elif v1.dir == 5: 
            return (angle if v2.values[1][0] < v1.values[1][0] else -angle) 

        # Determine if v2 is over or under v1
        if v2.values[1][1] > v1.calcLine(v2.values[1][0]): 
            return invert * angle
        elif v2.values[1][1] < v1.calcLine(v2.values[1][0]): 
            return -invert * angle

        # Edge case: v1 and v2 are parallel
        if v2.values[1][1] == v1.calcLine(v2.values[1][0]) and ((v2.values[1][0] < v1.values[1][0] and invert == -1) or (v2.values[1][0] > v1.values[1][0] and invert == 1)): 
            return 180.0
        
        elif v2.values[1][1] == v1.calcLine(v2.values[1][0]) and ((v2.values[1][0] > v1.values[1][0] and invert == -1) or (v2.values[1][0] < v1.values[1][0] and invert == 1)): 
            return 0.0
        
        return angle
        
        
            


    def removeDupPoints(self, points: list[list]) -> list[list]:
        """ 
        Removes duplicate points if angle is 180° or 0° 
        """
        
        if points is None or len(points) == 0: raise Exception("No points specified!")

        previousVector = Vector2D(points[0], points[1])

        for i, point in enumerate(points[1::], 1):
            v = Vector2D(points[i - 1], point)

            if v.values[1][1] == previousVector.calcLine(v.values[1][0]):
                points[i - 1] = [np.NaN, np.NaN]

            previousVector = v
            del v  
        return [point for point in points if point != [np.NaN, np.NaN]]
         


    def toSpikeCommands(self, points: list[list], map) -> None:
        """ 
        Converts coordinates to Spike commands 
        """

        # Check if points are empty
        if points is None or len(points) == 0: 
            print("No points in round")
            return 

        # Insert start point
        points.insert(0, list(self.convert_cords(([map.START_CORDS[0], map.START_CORDS[1] + 1]), map)))
        previousVector = Vector2D(points[0], points[1])

        # Iterate through points
        for i, point in enumerate(points[2::], 2):

            try: 
                v = Vector2D(points[i - 1], point)
            except: 
                continue
            
            print(f"db.gyroRotation({np.round(self.angleBetweenVectors(previousVector, v), 2)}, {self.speedValuesStraight[0]}, {self.speedValuesCurve[1]}, {self.speedValuesCurve[2]})")
            print(f"db.gyroStraightDrive({v.get_Length()}, {self.speedValuesStraight[0]}, {self.speedValuesStraight[1]}, {self.speedValuesStraight[2]})")
            
            previousVector = v
            del v


    def printCommands(self, map) -> None:
        """
        Prints Spike commands for every round
        """

        # Check if coordinates are empty
        if all(len(round) == 1 for round in map.coordinates):
            print("Coordinates empty!")
            return 

        # Set origin from top left to bottom left
        coordinates = [[list(self.convert_cords(points, map)) for points in round] for round in map.coordinates]
        
        for i, round in enumerate(coordinates, 1):
            if len(round) != 1:
                print(f"Round: {i}:")
                self.toSpikeCommands(round, map)

