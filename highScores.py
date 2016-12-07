import pygame, sys, json
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

display_width = 600
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

def scoreBoard():
    end_it=True
    clock = pygame.time.Clock()
    #--------Main Program Loop --------
    while end_it:
        #----- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #exit()
        #window.fill(BLACK)
        window.fill(WHITE)
        window.blit(loading, (0,0))
        #myfont=pygame.font.SysFont("Helvetica", 35, False, False)

        myfont = pygame.font.Font("freesansbold.ttf", 35)
        getScores()

        back = button("Back",300,450,175,75,blue, bright_blue, "back")
        if(back==False):
            end_it = False

        pygame.display.flip()
        clock.tick(60)

        # CLose the window and quit
    # pygame.quit()
    # sys.exit()

def setHighScore (level, mobs):
    # myfile = open("high_score.json", "r")
    # oldlist = []
    # #with open('high_score.json', 'r') as f:
    # for line in myfile:
    #     json_dict = json.loads(line)
    #     oldlist.append(json_dict[line])
    # myfile.close()
    # newlist = []
    with open('high_score.json') as f:
        data = json.load(f)

    newlist = []
    newdict = {}
    y=200
    #newlist = sorted(json_list, key=lambda k: k['level'], reverse=True)
    newlist = sorted(data["Players"], key=lambda k: k['score'], reverse=True)
    #myfile = open("high_score.json", "w")
    #y=200
    name = input("What is your name? ")
    #newlist = sorted(oldlist, key=lambda k: k['level'], reverse=True)
    myfile = open("high_score.json", "w")
    done = False
    for i in range(len(newlist)):
        theirname = newlist[i]
        if(name==theirname['name'] and theirname['score']>level and done==False):
            newlist[i]['level'] = level
            newlist[i]['score'] = mobs
            done = True
    if(done==False):
        newlist.append({"name":name, "level":level, "score": mobs})
    newdict["Players"] = newlist
    print(newlist, "\n", newdict)
    json.dump(newdict, myfile)
    #myfile.write(json_str)
    myfile.close()

def getScores():
    myfont = pygame.font.Font("freesansbold.ttf", 40)
    header1 = myfont.render("Name", True, BLACK)
    window.blit(header1,(50,140))
    header2 = myfont.render("Level", True, BLACK)
    window.blit(header2,(300,140))
    header3 = myfont.render("Score", True, BLACK)
    window.blit(header3,(480,140))
    myfont = pygame.font.Font("freesansbold.ttf", 35)
    # myfile = open("high_score.json", "r")
    # json_dict = json.loads(myfile).read()
    # json_list = []
    # for line in myfile:
    #     json_dict = json.loads(line)
    #     json_list.append(json_dict)
    #     #print(json_list)
    # myfile.close()
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