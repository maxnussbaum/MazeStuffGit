import gameStuff6, pygame, sys
from pygame import Color

pygame.init()
loading = pygame.image.load('highScorespic.png')

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
pygame.display.set_caption("High Scores")
window.blit(loading, (0,0))

def button(msg,x,y,w,h,ic,ac,action=None):
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
    smallText = pygame.font.SysFont("Helvetica", 40, True, False)
    newgame = smallText.render(msg, True, WHITE)
    space = smallText.size(msg)
    window.blit(newgame, (x+(w-space[0])/2,y+(h-space[1])/2,w,h))
    return True

def game_settings():
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
        window.fill(WHITE)
        window.blit(loading, (0,0))
        #myfont=pygame.font.SysFont("Helvetica", 35, False, False)

        myfont = pygame.font.Font("freesansbold.ttf", 35)
        #nlabel=myfont.render("Settings", True, BLACK)
        #window.blit(nlabel, (225,45))

        myfile = open("high_score.txt", "r")
        label = myfont.render(myfile.read(), True, BLACK)
        window.blit(label, (100,200))
        myfile.close()

        # mybuttonfont=pygame.font.SysFont("Helvetica", 35, False, False)
        # qlabel = mybuttonfont.render("Back", True, WHITE)

        back = button("Back",300,450,175,75,blue, bright_blue, "back")
        end_it = back
        #if (returntogame==False):
        #     end_it=False
        # elif (scores==False):
        #     end_it=False
        # else:
        #     window.blit(rtglabel, (295,175))
        #     window.blit(mmlabel, (335,325))
        #window.blit(qlabel, (365,475))

        pygame.display.flip()
        clock.tick(60)

        # CLose the window and quit
#pygame.register_quit(gameStuff.runMaze(MazeGenerator.main(msize, numrect, rectsize)))
    #pygame.quit()


def get_high_score():
    print

def main():
    myfile = open("high_score.txt", "r")
    game_settings()
    myfile.close()
