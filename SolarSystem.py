from Bodies import *
from math import sqrt
'''
Solar System object to manage the member bodies of the
system and advance time and orbits

@author: jsandy
'''

bigG = 6.67259e-11

class SolarSystem:
    '''
    classdocs
    '''

    def __init__(self, starType):
        '''
        Constructor
        '''
        self.bodies = []
        self.star = Star(starType)
        self.bodies.append(self.star)
        
        
    def addPlanet(self, planet):
        self.bodies.append(planet)
    
    def update(self):
        for body in self.bodies:
            (r, theta) = body.getPosition()
            
            #only update the planets, star doesnt move
            try:
                if r > 0:
                    omega = sqrt((bigG*self.star.mass) / (r*r*r))
                    
                    #update one day every frame:
                    body.advanceOrbit(60*60*24*omega)
            except ValueError:
                print(bigG*self.star.mass)
    
    def getBodies(self):
        return self.bodies
    
    #This method will create a solar system like our own
    # by adding planets that more or less match ours
    def autoPopulate(self):
        mecury = Planet(0.4, 3.3e+23, BodyColor.Grey)
        self.addPlanet(mecury)
        
        venus = Planet(0.7, 4.8e+24, BodyColor.Purple)
        self.addPlanet(venus)
        
        earth = Planet(1, 6.0e+24, BodyColor.Indigo)
        self.addPlanet(earth)
        
        mars = Planet(1.5,6.39e+23,BodyColor.Red)
        self.addPlanet(mars)
        
        jupiter = Planet(5.2,1.90e+27,BodyColor.Tan)
        self.addPlanet(jupiter)
        
        saturn = Planet(9.5,5.68e+26, BodyColor.Golden)
        self.addPlanet(saturn)
       
        
        
        