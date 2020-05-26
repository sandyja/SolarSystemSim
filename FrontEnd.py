'''

@author: jsandy
'''

import pygame
import sys
from math import cos, sin, sqrt

from SolarSystem import SolarSystem
from Bodies import StarType, BodyColor, BodySize, Body
from time import sleep

size = width, height = 1200, 900

def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode(size)
    
    mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
    largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
    
    solarSystem = None
    days = 0
    newDraw = True
    
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        screen.fill(BodyColor.Black.value)
        
        typeButtons = {}
        offset = 1
        
        for sType in StarType:
            typeButtons[sType] = pygame.Rect(offset *(width / 7), (height * 0.9), width / 8, 50)
            buttonText = mediumFont.render(sType.name, True, BodyColor.Black.value)
            buttonRect = buttonText.get_rect()
            buttonRect.center = typeButtons[sType].center
            pygame.draw.rect(screen,BodyColor.White.value, typeButtons[sType])
            screen.blit(buttonText, buttonRect)
            offset += 1
        
        #create a border to deliniate the buttons
        
        lineStart = (0, height*0.87)
        lineEnd = (width, height*0.87)    
        pygame.draw.line(screen,BodyColor.White.value, lineStart, lineEnd)
    
        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            for sType in StarType:
                if typeButtons[sType].collidepoint(mouse):
                    if solarSystem:
                        days = 0
                        del solarSystem
                        
                    newDraw = True
                    solarSystem = SolarSystem(sType)
                    solarSystem.autoPopulate()
        
            # Let user choose a starting Star.
        if solarSystem is None:
    
            # Draw title
            title = largeFont.render("Select a Star to Begin", True, BodyColor.White.value)
            titleRect = title.get_rect()
            titleRect.center = ((width / 2), 50)
            screen.blit(title, titleRect)
    
        else:
            title = largeFont.render(f"Solar System in motion... T+{days} days", True, BodyColor.White.value)
            titleRect = title.get_rect()
            titleRect.center = ((width / 2), 50)
            screen.blit(title, titleRect)
            
            solarSystem.update()
            days = days + 1
            drawBodies(solarSystem, screen, newDraw)
            newDraw = False
            
        pygame.display.update()
        pygame.display.flip()
        pygame.time.delay(10)
    
def drawBodies(solarSystem, screen, newDraw):
    for body in solarSystem.getBodies():
        (r, theta) = body.getPosition()
        (x,y) = convertToDrawCoords(r, theta)

        (size, color) = body.getDrawParams()
        (sX, sY) = convertToDrawCoords(0, 0)
        
        relX = x-sX
        relY = y-sY
        
        pygame.draw.circle(screen, color.value, (x,y), size.value)
        
        if r > 0 and newDraw:
            pygame.draw.circle(screen, color.value, (sX,sY), int(sqrt(relX*relX + relY*relY)), 1)
        
        

def convertToDrawCoords(bodyR, bodyTheta):
    #The bodies traveling in a polar coordinate system (R, theta). Convert 
    #here to an (x,y) frame that maps to our drawing canvas.
    
    #First convert to cartesian x,y:
    cartX = bodyR*cos(bodyTheta)
    cartY = bodyR*sin(bodyTheta)
    
    #Now, convert from solar system units of meters, to pixels. Here, we assume our canvas 
    # of 1200 pixels, is about the size of our own solar system, 30 AU, or 4.488e+12 meters
    solarSystemRadius =4.488e+12
    
    drawX = (width / solarSystemRadius) * cartX
    drawY = (width / solarSystemRadius) * cartY
    
    #Finally, move (0,0) to the center of the screen from the top left....
    drawX = drawX + width/2
    drawY = drawY + height/2
    
    #And bound them to the screen:
    
    if drawX > width:
        drawX = width
    elif drawX < 0:
        drawX = 0
        
    if drawY > height:
        drawY = width
    elif drawY < 0:
        drawY = 0
        
    return (int(drawX), int(drawY))
    
main()