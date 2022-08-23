import pygame
pygame.init()
font = pygame.font.SysFont('Constatia',30)

bg = (204,102,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

##define global valiriables
clicked = False

class Button():
    button_col = (255,0,0)
    hover_col = (75,255,255)
    click_col = (50,150,255)
    text_col = black
    width = 180
    height = 70

    def __init__(self,x,y,width,height,text):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        
    def draw(self,screen):
        global clicked
        action = False
        text_img = font.render(self.text,True,self.text_col)
##        get mouse position
        pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(self.x,self.y,text_img.get_width() + 10,self.height)

##        check mouseover and clicked condition
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen,self.click_col,button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen,self.hover_col,button_rect)


        else:
            pygame.draw.rect(screen,self.button_col,button_rect)

##        adding shading to button
            
        pygame.draw.line(screen,white,(self.x,self.y),(self.x + text_img.get_width()+ 10,self.y),2)
        pygame.draw.line(screen,white,(self.x,self.y),(self.x,self.y + self.height),2)
        pygame.draw.line(screen,black,(self.x,self.y + self.height),(self.x,self.y + self.height),2)
        pygame.draw.line(screen,black,(self.x + text_img.get_width() + 10,self.y),(self.x + text_img.get_width() + 10,self.y + self.height),2)

##        add text to button
        
        text_len = text_img.get_width()
        screen.blit(text_img,(self.x + (text_img.get_width()+ 5) // 2 - text_len //2,self.y + self.height//4))
        return action
