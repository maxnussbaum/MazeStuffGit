import gameStuff6, pygame, sys, settingsscreen
pygame.init()
loading = pygame.image.load('title_baconkid_gastronok.png')

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,40,180)

msize = 100
numrect = msize
rectsize = 30

display_width = 800
display_height = 600

#set the window size
window= pygame.display.set_mode((display_width, display_height) ,0,24)
pygame.display.set_caption("Dungeon Crawlers")
window.blit(loading, (0,0))

def button(msg,x,y,w,h,ic,ac,action=None):
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
    end_it=False
    clock = pygame.time.Clock()
    #--------Main Program Loop --------
    while (end_it==False):
        #----- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_it = True
        window.fill(BLACK)
        window.blit(loading, (200,100))
        myfont=pygame.font.SysFont("Calibri", 70, True, False)
        nlabel=myfont.render("Welcome to", False, WHITE)
        window.blit(nlabel, (225,45))


            #gameStuff.runMaze(MazeGenerator.main(msize, numrect, rectsize))

        newgame = button("New Game",150,450,130,50,green,bright_green, "play")
        loadgame = button("Load Game",350,450,130,50,red, bright_red)
        options = button("Options",550,450,130,50,blue, bright_blue,"settings")


        pygame.display.flip()
        clock.tick(60)

        # CLose the window and wuit
#pygame.register_quit(gameStuff.runMaze(MazeGenerator.main(msize, numrect, rectsize)))
    pygame.quit()

def main():
    game_intro()

main()
