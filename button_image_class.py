import pygame
#define global valiriables
clicked = False
class button():
    def __init__(self,button):
        self.button = button
        self.rect_btn = self.button.get_rect()
        self.rect = pygame.Rect(self.rect_btn.x,self.rect_btn.y,self.rect_btn.width,self.rect_btn.height)
    def draw(self,screen,x,y):
        self.rect = pygame.Rect(x,y,self.rect_btn.width,self.rect_btn.height)
        global clicked
        action = False
        screen.blit(self.button,(x,y))
        
##        get mouse position
        pos = pygame.mouse.get_pos()
##        check mouseover and clicked condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
        
        return action
