import pygame, sys, json
from pygame import Color

pygame.init()
loading = pygame.image.load('highScorespic.png')
loading = pygame.transform.scale(loading, (600,119,))

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

display_width = 600
display_height = 600

window= pygame.display.set_mode((display_width, display_height) ,0,24)
pygame.display.set_caption("High Scores")
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

def scoreBoard():
    '''
    Creates a button and sets up the High Score screen and calls getScores()
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
        #window.fill(BLACK)
        window.fill(WHITE)
        window.blit(loading, (0,0))
        #myfont=pygame.font.SysFont("Helvetica", 35, False, False)

        myfont = pygame.font.Font("freesansbold.ttf", 35)
        getScores()

        back = button("Back",210,450,175,75,blue, bright_blue, "back")
        if(back==False):
            end_it = False

        pygame.display.flip()
        clock.tick(60)

        # CLose the window and quit
    # pygame.quit()
    # sys.exit()

def setHighScore (level, mobs):
    '''
    Creates a new high score when you click the x button during a game
    args:       level     -   (int)The last level the player completed
                mob       -   (int)The number of zombies they killed
    return:
    '''

    with open('high_score.json') as f:
        data = json.load(f)

    newlist = []
    newdict = {}
    y=200
    newlist = sorted(data["Players"], key=lambda k: k['score'], reverse=True)
    name = input("What is your name? ")
    myfile = open("high_score.json", "w")
    done = False
    for i in range(len(newlist)):
        theirname = newlist[i]
        if(name==theirname['name'] and theirname['score']<mobs and done==False):
            newlist[i]['level'] = level
            newlist[i]['score'] = mobs
            done = True
    if(done==False):
        newlist.append({"name":name, "level":level, "score": mobs})
    newdict["Players"] = newlist
    #print(newlist, "\n", newdict)
    json.dump(newdict, myfile)
    myfile.close()

def getScores():
    '''
    Gets the scores from the high score file and displays it in the window
    args:
    return:
    '''
    myfont = pygame.font.Font("freesansbold.ttf", 40)
    header1 = myfont.render("Name", True, BLACK)
    window.blit(header1,(50,140))
    header2 = myfont.render("Level", True, BLACK)
    window.blit(header2,(300,140))
    header3 = myfont.render("Score", True, BLACK)
    window.blit(header3,(480,140))
    myfont = pygame.font.Font("freesansbold.ttf", 35)
    with open('high_score.json') as f:
        data = json.load(f)

    newlist = []
    y=200
    #newlist = sorted(json_list, key=lambda k: k['level'], reverse=True)
    newlist = sorted(data["Players"], key=lambda k: k['score'], reverse=True)
    #myfile = open("high_score.json", "w")


    if len(newlist)>=5:
        for i in range(5):
            name = newlist[i]["name"]
            level = str(newlist[i]["level"])
            score = str(newlist[i]["score"])
            label1 = myfont.render(name, True, BLACK)
            label2 = myfont.render(level, True, BLACK)
            label3 = myfont.render(score, True, BLACK)
            window.blit(label1, (50,y))
            window.blit(label2, (310,y))
            window.blit(label3, (490,y))
            y+=50
    else:
        for i in range(len(newlist)):
            name = newlist["Players"][i]["name"]
            level = str(newlist["Players"][i]["level"])
            score = str(newlist["Players"][i]["score"])
            label1 = myfont.render(name, True, BLACK)
            label2 = myfont.render(level, True, BLACK)
            label3 = myfont.render(score, True, BLACK)
            window.blit(label1, (100,y))
            window.blit(label2, (350,y))
            window.blit(label3, (550,y))
            y+=50


def main():
    scoreBoard()
