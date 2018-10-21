import pygame
import sys
pygame.init()

display_width = 500
display_height = 300

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Learning Snapdragon")

background_image = pygame.image.load("images\dragonboard410c.jpg").convert()


def text_objects(text, font):
    textSurface = font.render(text, True, green)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('comicsans',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

def button(msg,x,y,h,w,ic,ac,action=None):
       mouse = pygame.mouse.get_pos()
       click = pygame.mouse.get_pressed()

       if (((x)+(h)) > mouse[0] > (x) and ((y)+(w)) > mouse[1] > (y)):
           pygame.draw.rect(gameDisplay, ac,(x,y,h,w))

           if click[0] == 1 and action != None:
               if action == "Play":
                   game_loop2()
               elif action == "quit":
                   pygame.quit()
                   quit()

       else:
           pygame.draw.rect(gameDisplay, ic,(x,y,h,w))

       largeText = pygame.font.Font('freesansbold.ttf',20)
       TextSurf, TextRect = text_objects(msg, largeText)
       TextRect.center = ((x+h/2),(y+w/2))
       gameDisplay.blit(TextSurf, TextRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.blit(background_image,[0,0])
        largeText = pygame.font.Font('freesansbold.ttf',40)
        TextSurf, TextRect = text_objects("Basics Of Snapdragon", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        button1=button("Snapdragon projects",50,200,250,25,white,red,"Play")
        button2=button("Overlook of Snapdragon",50,250,250,25,white,red,"Play")

        pygame.display.update()
        clock.tick(15)
        
game_intro()
pygame.quit()
quit()

