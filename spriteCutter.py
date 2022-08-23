import pygame

class Sprite:
    def getSprite(image,width,height,total_number_of_images,color_key,scale = 1):
        image_list = []
        image_surface = pygame.Surface((width,height)).convert_alpha()
        for i in range(total_number_of_images):
            image_surface.blit(image,(0,0),(width * i,0,width,height))
            image_surface.set_colorkey((color_key))
##if you want to scale automatic by bass a scale at what size use this
##            first you will take a scale variable from the peremter list
##            image_surface = pygame.transform.scale(image_surface,(width* scale,height*scale))
            image_surface = pygame.transform.scale(image_surface,(width * scale,height * scale))
            image_list.append(image_surface)
        return image_list

    def getImage(imageSprite,width,height,number_of_the_image_in_a_picture,color_key):
        image = pygame.Surface((width,height)).convert_alpha()
        image.set_colorkey(color_key)
        image.blit(imageSprite,(0,0),((number_of_the_image_in_a_picture * width),0,width,height))
        return image
