import pygame

pygame.init()
loading = pygame.image.load('settings_logo_png.png')

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

display_width = 800
display_height = 600

window= pygame.display.set_mode((display_width, display_height) ,0,24)
pygame.display.set_caption("Settings")
window.blit(loading, (0,0))

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))
        if(click[0] == 1 and action != None):
            if action=="play":
                gameStuff.main()
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))

def game_settings():
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
        myfont=pygame.font.SysFont("Helvetica", 100, False, False)
        nlabel=myfont.render("Settings", True, BLACK)
        window.blit(nlabel, (225,45))

        mybuttonfont=pygame.font.SysFont("Helvetica", 35, False, False)
        rtglabel = mybuttonfont.render("Return To Game", True, WHITE)
        mmlabel = mybuttonfont.render("Main Menu", True, WHITE)
        qlabel = mybuttonfont.render("Quit", True, WHITE)

        returntogame = button("Return To Game",300,150,200,75,blue,bright_blue)
        mainmenu = button("Main Menu",300,300,200,75,blue, bright_blue)
        quit = button("Quit",300,450,200,75,blue, bright_blue)

        window.blit(rtglabel, (305,175))
        window.blit(mmlabel, (335,325))
        window.blit(qlabel, (365,475))

        pygame.display.flip()
        clock.tick(60)

        # CLose the window and quit
#pygame.register_quit(gameStuff.runMaze(MazeGenerator.main(msize, numrect, rectsize)))
    pygame.quit()

def main():
    game_settings()




main()
