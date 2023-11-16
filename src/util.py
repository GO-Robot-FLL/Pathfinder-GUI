from src.vector import Vector2D, np
from src.constants import Constants as c


class Util:

    def __init__(self):
        self.speedValuesStraight = (40, 50, 40)
        self.speedValuesCurve = (40, 40, 40)

    def convert_cords(self, cords, map) -> list:
        """ Converts pixel coordinates """
        """ (0, 0) is bottom left, scaling to cm applied"""
        return cords[0] * map.X_SCALE, (c.SCREEN_HEIGHT - cords[1]) * map.Y_SCALE
    
    def angleBetweenVectors(self, v1: Vector2D, v2: Vector2D) -> float:
        """ Calculates turning angle using vector angles """
        """ Checkes if y-Cord of v2 is over/under/on v1 based on dir """
        # m1 = v1.getSlope()
        # m2 = v2.getSlope()
        # angle = round(np.degrees(np.arctan((m1 - m2)/(1 + m1 * m2))), 1)
        angle = np.degrees(np.arccos(np.clip(np.dot(v1.get_unitVector(), v2.get_unitVector()), -1.0, 1.0)))
        invert = (-1 if 2 <= v1.dir <= 4 else 1)

        # if v2.values[1][1] == v1.calcLine(v2.values[1][0]) and v2.get_Slope() == -v1.get_Slope(): return 180.0
        # elif v2.values[1][1] == v1.calcLine(v2.values[1][0]) and v2.get_Slope() == v1.get_Slope(): return 0.0

        if v1.dir == 1: return (-angle if v2.values[1][0] < v1.values[1][0] else angle) 
        elif v1.dir == 5: return (angle if v2.values[1][0] < v1.values[1][0] else -angle) 

        if v2.values[1][1] > v1.calcLine(v2.values[1][0]): return invert * angle
        elif v2.values[1][1] < v1.calcLine(v2.values[1][0]): return -invert * angle
        
        
        if v2.values[1][1] == v1.calcLine(v2.values[1][0]) and ((v2.values[1][0] < v1.values[1][0] and invert == -1) or (v2.values[1][0] > v1.values[1][0] and invert == 1)): return 180.0
        elif v2.values[1][1] == v1.calcLine(v2.values[1][0]) and ((v2.values[1][0] > v1.values[1][0] and invert == -1) or (v2.values[1][0] < v1.values[1][0] and invert == 1)): return 0.0
            


    def removeDupPoints(self, points: list[list]) -> list[list]:
        """ Removes duplicate points if angle is 180° or 0° """
        

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
        """ Converts coordinates to Spike commands """


        if points is None or len(points) == 0: 
            print("No points in round")
            return 

        points.insert(0, list(self.convert_cords(([map.START_CORDS[0], map.START_CORDS[1] + 1]), map)))
        previousVector = Vector2D(points[0], points[1])

        for i, point in enumerate(points[2::], 2):

            try: 
                v = Vector2D(points[i - 1], point)
            except: 
                continue
            
            # print(previousVector.print(), v.print())
            # print(v.values[1][1] == previousVector.calcLine(v.values[1][0]), previousVector.get_Slope(), v.get_Slope())
            print(f"db.gyroRotation({np.round(self.angleBetweenVectors(previousVector, v), 2)}, {self.speedValuesStraight[0]}, {self.speedValuesCurve[1]}, {self.speedValuesCurve[2]})")
            print(f"db.gyroStraightDrive({v.get_Length()}, {self.speedValuesStraight[0]}, {self.speedValuesStraight[1]}, {self.speedValuesStraight[2]})")
            
            previousVector = v
            del v


    def printCommands(self, coordinates, map):
        
        if all(len(round) == 1 for round in coordinates):
            print("Coordinates empty!")
            return 
    
        coordinates = [[list(self.convert_cords(points, map)) for points in round] for round in coordinates]
        
        for i, round in enumerate(coordinates, 1):
            if len(round) != 1:
                print(f"Round: {i}:")
                self.toSpikeCommands(round, map)

