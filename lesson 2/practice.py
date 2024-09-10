import pygame
pygame.init()

screen = pygame.display.set_mode((800,800))

class Circle():
    def __init__(self, color, dimensions, radius):
        self.color = color
        self.dimensions = dimensions
        self.radius = radius
        self.surface = screen

    def drawCircle(self):
        self.circle_draw = pygame.draw.circle(self.surface, self.color, self.dimensions, self.radius)

redCircle = Circle("red", (50, 20), 50)
redCircle.drawCircle()

greenCircle = Circle("green", (430, 350), 100)
greenCircle.drawCircle()

while True:
    pygame.display.update()
