import math
from map import Map
class Import:
    def __init__(self):
        self.round_commands = [ 'gyroRotation(45,30,30,30)', 'gyroStraightDrive(50,30,30,30)', 'gyroStraightDrive(50,30,30,30)', 'gyroStraightDrive(70,30,30,30)']
        self.distance = ''
        self.angle = 90
        self.turn_angle = '0'
        self.count = 0
        self.count2 = 0
        self.courrent_count = 0
        self.r = 0
        self.map1 = Map()
        self.current_coardinates = (0,0)
        pass

    def import_round(self):
        
        self.round_commands = []

        running = True
        while running:
            command = input("input command: ")
            if command == "":
                running = False

            else:
                self.round_commands.append(command)  
        for i in self.round_commands :
            if "gyroStraightDrive" in i:
                self.count2 += 1




    
    def calculate_coardinates(self,xy,al):
        
        """
        Calculate the intersection point of the circle with radius "length" and the linear function mimicking the slope "angle"

        xy x-startkoardinate, y-startkoardinate
        al angel, length
        r länge
        """
        h, k = xy
        print(al[0])
        if al[0] == 90:
            coardinates = (0,xy[1] + al[1])
            return coardinates
        elif al[0] == 0:
            print("test")
            coardinates = (xy[0] + al[1],0)
            return coardinates
        elif al[0] < 0:
            print("test")
        else:
            # Steigung berechnen
            m = round(math.tan(math.radians(al[0])),3)
            r = al[1]
            y = round(k - m * h,3)

            a = 1 + m**2
            b = -2*h + 2*m*y - 2*m*k
            c = h**2 + y**2 - 2*y*k + k**2 - r**2

            x1 = (-b + math.sqrt(b**2 - 4*a*c))/ (2*a)  #calculation of x1 using Quadratic Formula
            #x2 = (-b - math.sqrt(b**2 - 4*a*c))/ (2*a)
    
            coardinates = (x1,(m*x1 + y))
        return coardinates








    def read_code(self):
        gyroRotation = False
        self.count = 0
        for i in self.round_commands:
            self.count += 1

        if self.count == self.courrent_count:
            return False

        for e in range(self.count):
            running = True
            e += self.courrent_count
            i = self.round_commands[e]
            if "gyroStraightDrive" in i:
                x = 18
                gyroRotation = False
                self.distance = ''
                
                while running:
                    self.distance = str(self.distance)
                    self.distance += i[x]
                    x += 1
                    if i[x] == ',' or i[x] == ")":
                        running = False
                        self.distance = int(self.distance)
                        
            elif "gyroRotation" in i:
                x = 13
                running = True
                gyroRotation = True
                self.distance = '0'
                self.turn_angle = '0'
                while running:
                    self.turn_angle += i[x]
                    x += 1
                    if i[x] == ',' or i[x] == ")":
                        self.angle -= int(self.angle)
                        running = False
            if gyroRotation == False:
                self.courrent_count = 0
                self.courrent_count += (e + 1)
                return int(self.angle), self.distance
        pass


    def process(self):
        self.read_code_data = []
        self.count2 = 3
        #self.import_round()
        for i in range(self.count2):
            self.read_code_data.append(self.read_code())
        #print(self.read_code())
        for i in self.read_code_data:
            self.current_coardinates = self.calculate_coardinates(self.current_coardinates,(45,5))
            print(self.current_coardinates)

        

import1 = Import()
import1.process()
#print(import1.calculate_coardinates((0,0),(45,5)))