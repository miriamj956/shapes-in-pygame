import pygame
pygame.init()

#set width and height
screen=pygame.display.set_mode((800,600))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen.fill("skyblue")

class Rect():
    def __init__(self, color, dimension):
        self.color = color
        self.dimension = dimension
        self.surface = screen
    
    def drawRect(self):
        self.rect_draw = pygame.draw.rect(self.surface, self.color, self.dimension)

        
#Object
#x,y,w,h
greenRect = Rect(green, (50, 20, 100, 120))
#objectname.function name
greenRect.drawRect()

redRect = Rect(red, (200, 100, 150, 150))
redRect.drawRect()

blackRect = Rect(black, (400, 70, 100, 20))
blackRect.drawRect()

blueRect = Rect(blue, (600, 300, 170, 100))
blueRect.drawRect()

purpleRect = Rect("purple", (430, 350, 100, 100))
purpleRect.drawRect()


while True:
    pygame.display.update()