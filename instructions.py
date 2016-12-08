#designed and coded by Jacqueline St Pierre
import pygame, sys
pygame.init()

bright_red = (60,0,0)
WHITE    = ( 255, 255, 255)
blue = (0,0,255)
bright_blue = (0,40,180)

msize = 100
numrect = msize
rectsize = 30

display_width = 600
display_height = 600

window= pygame.display.set_mode((display_width, display_height) ,0,24)
pygame.display.set_caption("High Scores")

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
            if action=="back":
                return False
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 35)
    #smallText = pygame.font.SysFont("Helvetica", 40, True, False)
    newgame = smallText.render(msg, True, WHITE)
    space = smallText.size(msg)
    window.blit(newgame, (x+(w-space[0])/2,y+(h-space[1])/2,w,h))
    return True

def instructions():
    '''
    Creates a button and sets up the Instructions screen with all of the instructions
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
                pygame.quit()
                exit()
                end_it=False
        window.fill(bright_red)
        #myfont=pygame.font.SysFont("Helvetica", 35, False, False)

        myfont = pygame.font.Font("freesansbold.ttf", 55)
        newgame = myfont.render("Instructions", True, WHITE)
        window.blit(newgame, (120,30))
        myfont = pygame.font.Font("freesansbold.ttf", 25)
        rules1 = myfont.render("Navigate the maze and try to find the pink", True, WHITE)
        rules2 = myfont.render("squares to advance to the next level.", True, WHITE)
        rules3 = myfont.render("The objective of the game is to kill", True, WHITE)
        rules4 = myfont.render("the most zombies.", True, WHITE)
        rules5 = myfont.render("Press 'O' during the game for the options", True, WHITE)
        rules6 = myfont.render("screen.", True, WHITE)
        rules7 = myfont.render("Press the red 'X' to exit out of the", True, WHITE)
        rules8 = myfont.render("game and save your high score.", True, WHITE)
        rules9 = myfont.render("Press quit in options to exit out of the", True, WHITE)
        rules10 = myfont.render("game without saving score.", True, WHITE)
        window.blit(rules1,(25,100))
        window.blit(rules2,(25,140))
        window.blit(rules3,(25,180))
        window.blit(rules4,(25,220))
        window.blit(rules5,(25,260))
        window.blit(rules6,(25,300))
        window.blit(rules7,(25,340))
        window.blit(rules8,(25,380))
        window.blit(rules9,(25,420))
        window.blit(rules10,(25,460))

        end_it = button("Back",210,500,175,75,blue, bright_blue, "back")
        # if(back==False):
        #     end_it = False

        pygame.display.flip()
        clock.tick(60)
    # CLose the window and quit
    #pygame.quit()
    # sys.exit()

def main():
    instructions()
