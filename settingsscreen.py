#Anna
import pygame, sys, highScores, instructions
from pygame import Color

pygame.init()
loading = pygame.image.load('settings_logo_png.png')
display_width = 600
display_height = 600
window= pygame.display.set_mode((display_width, display_height) ,0,24)
pygame.display.set_caption("Settings")
window.blit(loading, (0,0))

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

blue = (0,50,120)

bright_blue = (0,80,100)

msize = 100
numrect = msize
rectsize = 30



def button(msg,x,y,w,h,ic,ac,action=None):
    '''
    Creates a button with font centered in it and functionality
    args:       msg     -   (str) text to be put on the button
                x       -   (int)x coordinate
                y       -   (int)y coordinate
                w       -   (int)width of the button
                h       -   (int)height of the button
                ic      -   (tuple)the numbers to decide on the lighter color when mouse isn't hovering over button
                ac      -   (tuple)the numbers for the color when mouse is hovering over button
                action  -   (str)word for what the button should do when clicked
    return:     returns True or False to decide whether or not to close the window
    '''
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))
        if(click[0] == 1 and action != None):
            if action=="instructions":
                instructions.main()
                #return True
            elif action=="back":
                return False
            elif action=="quit":
                return False
            elif action=="scores":
                highScores.main()
                #return True
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))
    pygame.font.init()
    smallText = pygame.font.Font("freesansbold.ttf", 35)
    #smallText = pygame.font.SysFont("Helvetica", 35, True, False)
    newgame = smallText.render(msg, True, WHITE)
    space = smallText.size(msg)
    window.blit(newgame, (x+(w-space[0])/2,y+(h-space[1])/2,w,h))
    return True

def game_settings():
    '''
    Creates the buttons and sets up the Settings screen
    args:
    return:
    '''
    end_it=True
    clock = pygame.time.Clock()
    #--------Main Program Loop --------
    while end_it:
        #----- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #end_it = True
                pygame.quit()
                exit()
        #window.fill(BLACK)
        #fourth zero makes it transparent but it doesn't work in showing
        #the screen under it to act as a clear screen
        empty = Color(0,0,0,0)
        window.fill(empty)
        window.blit(loading, (0,0))
        myfont=pygame.font.SysFont("Helvetica", 100, False, False)
        nlabel=myfont.render("Settings", True, BLACK)
        window.blit(nlabel, (170,45))

        mybuttonfont=pygame.font.SysFont("Helvetica", 35, False, False)

        rules = button("Instructions",70,200,220,75,blue,bright_blue, "instructions")
        scores = button("High Scores",350,200,205,75,blue, bright_blue, "scores")
        back = button("Back",80,370,200,75,blue, bright_blue, "back")
        quit = button("Quit",350,370,200,75,blue, bright_blue, "quit")
        #end_it = back
        if (back==False):
            end_it=False


        pygame.display.flip()
        clock.tick(60)

        if(quit==False):
            pygame.quit()
            exit()

        # CLose the window and quit
#pygame.register_quit(gameStuff.runMaze(MazeGenerator.main(msize, numrect, rectsize)))
    #pygame.quit()

def main():
    game_settings()
