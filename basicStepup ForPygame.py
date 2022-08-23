import pygame
import random
from color import Color
from text import Text
from math import *

pygame.init()
text = ''
width = 500
height = 500

screen = pygame.display.set_mode((width,height))

def mainLoop():
    global text
    run = True
    while run:
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                text += event.unicode
        text_render = Text(50,100,text,Color.Red,15)
        text_render.draw(screen)
        
        pygame.display.flip()

mainLoop()
