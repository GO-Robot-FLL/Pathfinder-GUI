import numpy as np


class Vector2D:
    def __init__(self, *args) -> None:
        """
        Each vector is defined by two points: (x1, y1) and (x2, y2)
        Example: Vector2D((0, 0), (1, 1)) -> Vector from (0, 0) to (1, 1)
        """
        
        if len(args) == 0: self.values = (0, 0)
        else: self.values = args
        if self.values[0] == self.values[1]: raise Exception("Same start and end point")
        self.deltaY = self.values[1][1] - self.values[0][1]
        self.deltaX = self.values[1][0] - self.values[0][0]
        self.init_dir()


    def print(self) -> None:
        """ 
        Prints the Vector 
        """

        print(f"Values={self.values}, Dir={self.dir}, Slope={self.get_Slope()}, Length={self.get_Length()}")


    def init_dir(self):
        """ 
        Initializes the direction of the vector 
        """

        if self.get_Slope() == np.inf: self.dir = 1  # Up
        if self.get_Slope() == -np.inf: self.dir = 5 # Down
        if self.get_Slope() == 99999: self.dir = 3    # Right
        if self.get_Slope() == -99999: self.dir = 7    # Left
        if self.deltaX > 0 and self.deltaY > 0: self.dir = 2    # Top right
        if self.deltaX > 0 and self.deltaY < 0: self.dir = 4    # Bottom right
        if self.deltaX < 0 and self.deltaY < 0: self.dir = 6    # Bottom left
        if self.deltaX < 0 and self.deltaY > 0: self.dir = 8    # Top left


    def get_Angle(self) -> float:
        """ 
        Returns angle between vector and x-axis in degrees 
        """

        return np.round(np.degrees(np.arctan(self.deltaY / self.deltaX)), 2)


    def get_Length(self) -> float:
        """ 
        Returns the magnitude (length) of the vector 
        """

        return np.round(np.sqrt(self.deltaY**2 + self.deltaX**2), 2)
    

    def get_unitVector(self) -> float:
        """ 
        Returns the unit vector 
        """

        return (self.deltaX, self.deltaY) / np.linalg.norm((self.deltaX, self.deltaY))
    

    def get_Slope(self) -> float:
        """ 
        Returns the slope of the vector 
        """

        try: 
            slope = self.deltaY / self.deltaX
            if slope == 0 and self.deltaX > 0: return 99999
            elif slope == 0 and self.deltaX < 0: return -99999
            else: return slope
        except ZeroDivisionError:
            if self.deltaY >= 0: return np.inf
            else: return -np.inf


    def calcLine(self, x: float) -> float:
        """ 
        Returns the y value of line equation of the vector 
        """
        
        return self.get_Slope() * x + self.values[0][1] - self.get_Slope() * self.values[0][0] 

