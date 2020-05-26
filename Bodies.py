from enum import Enum
from math import pi

'''

@author: jsandy
'''

solMass = 2.0e+30
astroUnit = 1.496e+11

class BodySize(Enum):
    Tiny = 2
    Little = 3
    Small = 4
    Normal = 6
    Large = 8
    Huge = 15
    Gigantic = 25
    
class BodyColor(Enum):
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Yellow = (255, 255, 51)
    Red = (255, 0, 0)
    Blue = (0, 0, 255)
    Green = (0, 255 ,0)
    Purple = (102, 0, 102)
    Indigo = (51, 255, 255)
    Rust = (153, 0, 0)
    Tan = (153, 76, 0)
    Golden = (226, 206, 24)
    Grey = (196, 196, 194)
    
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class StarType(Enum):
    SuperGiant = (16, 6.6, BodyColor.Blue, BodySize.Gigantic)
    Giant = (8, 3.8, BodyColor.Blue, BodySize.Huge)
    Large = (4, 2, BodyColor.White, BodySize.Large)
    Sol = (1, 1, BodyColor.Yellow, BodySize.Normal)
    Dwarf = (0.5, 0.7, BodyColor.Red, BodySize.Small)
    
    def __init__(self, mass, radius, bodyColor, bodySize):
        self.mass = mass       # Solar Masses
        self.radius = radius   # Solar Radii
        self.color = bodyColor
        self.size = bodySize
    

class Body:
    '''
    classdocs
    '''     

    def __init__(self, initR, mass, drawSize, drawColor):
        '''
        Constructor
        '''
        self.posR = initR
        self.posTheta = 0
        self.mass = mass
        self.drawSize = drawSize
        self.drawColor = drawColor
    
    def __hash__(self):
        return hash((self.posR, self.mass, self.posTheta))
    
    def getPosition(self):
        return (self.posR, self.posTheta)
    
    def getDrawParams(self):
        return (self.drawSize, self.drawColor)
    
    def advanceOrbit(self, deltaTheta):
        self.posTheta = self.posTheta + deltaTheta
        if self.posTheta >= 2*pi:
            self.posTheta = 0
        

class Planet(Body):
    
    def __init__(self, initR, mass, drawColor):
        size = BodySize.Tiny
        if mass < 1.0e+24:
            size = BodySize.Tiny
        elif mass < 1.0e+25:
            size = BodySize.Little
        else:
            size = BodySize.Small
        
        super().__init__(initR*astroUnit, mass, size, drawColor)
        
        
class Star(Body):
    
    def __init__(self, starType):
        super().__init__(0, starType.mass*solMass, starType.size, starType.color)
        self.posTheta = 0
        
    def getPosition(self):
        return (0,0)
        
        
        