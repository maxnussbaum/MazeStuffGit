import gameStuff6, pygame, sys, settingsscreen
pygame.init()
loading = pygame.image.load('startscreen600x600.png')

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
red = (125,0,20)
green = (0,200,0)
blue = (0,0,255)

bright_red = (60,0,0)
bright_green = (0,255,0)
bright_blue = (0,40,180)

msize = 100
numrect = msize
rectsize = 30

display_width = 600
display_height = 600

#set the window size
window= pygame.display.set_mode((display_width, display_height) ,0,24)
pygame.display.set_caption("Dungeon Crawlers")
window.blit(loading, (0,0))

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
    # print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))
        if(click[0] == 1 and action != None):
            if action=="play":
                gameStuff6.main()
            if action=="settings":
                settingsscreen.main()
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))


    smallText = pygame.font.SysFont("Helvetica", 28, True, False)
    newgame = smallText.render(msg, True, WHITE)
    space = smallText.size(msg)
    window.blit(newgame, (x+(w-space[0])/2,y+(h-space[1])/2,w,h))

def game_intro():
    '''
    Creates buttons and sets up the main screen and sets the background
    args:
    return:
    '''
    end_it=False
    clock = pygame.time.Clock()
    #--------Main Program Loop --------
    while (end_it==False):
        #----- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_it = True
        window.fill(BLACK)
        window.blit(loading, (0,0))
        myfont=pygame.font.SysFont("Calibri", 70, True, False)
        nlabel=myfont.render("Welcome to", False, WHITE)
        window.blit(nlabel, (130,45))


            #gameStuff.runMaze(MazeGenerator.main(msize, numrect, rectsize))

        newgame = button("New Game",150,450,130,50,red,bright_red, "play")
        #options = button("Options",350,450,130,50,red, bright_red, "settings")
        options = button("Options",350,450,130,50,red, bright_red,"settings")


        pygame.display.flip()
        clock.tick(60)

        # CLose the window and wuit
#pygame.register_quit(gameStuff.runMaze(MazeGenerator.main(msize, numrect, rectsize)))
    pygame.quit()

def main():
    game_intro()

main()
