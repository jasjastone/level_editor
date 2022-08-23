import pygame
pygame.init()
pygame.font.init()
class Text():
    
    def __init__(self,x,y,text,color,font_size):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont("Courier New",font_size)
    def draw(self,screen):
        text_img = self.font.render(self.text,False,self.color)
        screen.blit(text_img,(self.x,self.y))
