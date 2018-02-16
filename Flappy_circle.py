import os

from Bird import Bird
from Wall import Wall


def reset():
    global score
    
    score = 0
    bird.__init__()
    wall1.__init__()
    wall2.__init__()
    wall2.x = screen_width+(screen_width/6)
    wall3.__init__()
    wall3.x = screen_width+(2*screen_width/6)
    wall4.__init__()
    wall4.x = screen_width+(3*screen_width/6)
    wall5.__init__()
    wall5.x = screen_width+(4*screen_width/6)
    wall6.__init__()
    wall6.x = screen_width+(5*screen_width/6)
    still_screen()

    time.sleep(1)

def save_it(high_score):
    name = raw_input("Name: ")
    fob = open("highscores_flappy_bird.txt","a")
    if high_score < 10:
        fob.write(str(0)+str(high_score)+": "+name+"\n")
    else:    
        fob.write(str(high_score)+": "+name+"\n")
    fob.close()
    print ("High score saved in Highscores_flappy_bird.txt")
    return()

def save():
    try:
        save = raw_input("Do you want to save?[Y/N]: ")
    except:
        save()
    return (save)

def read_it():
    fob = open("highscores_flappy_bird.txt","r")
    scores = fob.readlines()
    return(scores)
def sort_it():
    scores = read_it()
    scores = sorted(scores,reverse = True)
    return(scores)

def save_new_scores(scores):
    fob2 = open("highscores_bouncing_ball.txt","w")
    fob2.writelines(scores)
    fob2.close()
    
    return()
def still_screen():
    while True:
        screen.blit(background,(0,0))
        bird.draw()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return()
        pause_text = font.render("Press SPACE to play",True,white)
        screen.blit(pause_text,((screen_width/2)-70,screen_height/2))
        scores = sort_it()
        high_score = scores[0]
        high_score = high_score[:-1]
        high_score_text = font.render("High Score - "+str(high_score),True,white)
        screen.blit(high_score_text,((screen_width/2)-70,(screen_height/2-70)))
        

        pygame.display.update()
                
    

import pygame

quit_it = False

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
pygame.mixer.music.load('Zombie Nation - Kernkraft 400.mp3')
pygame.mixer.music.play(-1,31.0)

flap = pygame.mixer.Sound("sfx_wing.mp3")
hit = pygame.mixer.Sound('sfx_hit.mp3')
point = pygame.mixer.Sound('sfx_point.mp3')
gap_change = pygame.mixer.Sound('smb_coin.mp3')


        
#game loop    
while True:
    
    import pygame, sys
    from pygame.locals import *
    import time
    
    
    #screen sizes
    screen_width = 1000
    screen_height = 600

    
    
    
    

    #colours
    black = (0,0,0)
    white = (250,250,250)
    red = (250,0,0)
    green = (0,250,0)
    blue = (0,0,250)

    clock = pygame.time.Clock()
    font = pygame.font.Font(None,40)

    walls = []
    high_scores=[0]
    score = 0
    lives = 5
    FPS = 30
    gap_length = 75
    score_text = font.render(str(score),True,white)


    background = pygame.image.load("video games super mario backgrounds 2560x1024 wallpaper_www.wallmay.net_65.jpg")
    #set up window
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (8,30)#widnow pop up pos
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("flappy_bird")
    background = pygame.transform.smoothscale(background,(screen_width,screen_height))#resize

    
    
    



        

    #define bird and walls
    #place walls apart

    bird = Bird()
    wall1 = Wall()
    wall2 = Wall()
    wall2.x = screen_width+(screen_width/6)
    wall3 = Wall()
    wall3.x = screen_width+(2*screen_width/6)
    wall4 = Wall()
    wall4.x = screen_width+(3*screen_width/6)
    wall5 = Wall()
    wall5.x = screen_width+(4*screen_width/6)
    wall6 = Wall()
    wall6.x = screen_width+(5*screen_width/6)
    #add walls to a list
    walls.append(wall1)
    walls.append(wall2)
    walls.append(wall3)
    walls.append(wall4)
    walls.append(wall5)
    walls.append(wall6)
    
    time.sleep(1)
    pygame.mixer.init()

    still_screen()
        
    

    #animation loop
    while True:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flap.play()
                    #flap - jump up
                    bird.speed = -10
        #terminal velocity       
        if bird.speed <10:
            #increase falling speed
            bird.jump()
        

        bird.movement()
        bird.draw()
        for item in walls:
            item.movement(score)
            item.draw()
            #wall collisions
            if item.top.collidepoint(bird.center[0]+5,bird.center[1]+5) or item.top.collidepoint(bird.center[0]-5,bird.center[1]-5) or item.top.collidepoint(bird.center[0]+5,bird.center[1]-5) or item.top.collidepoint(bird.center[0]-5,bird.center[1]+5) or item.bottom.collidepoint(bird.center[0]+5,bird.center[1]+5) or item.bottom.collidepoint(bird.center[0]-5,bird.center[1]-5) or item.bottom.collidepoint(bird.center[0]+5,bird.center[1]-5) or item.bottom.collidepoint(bird.center[0]-5,bird.center[1]+5):
                high_scores.append(score)
                hit.play()
                reset()
                lives -=1
        #wall spacing
        for item in walls:
            if item.x == screen_width/6 or item.x == (screen_width/6)+1 or item.x == (screen_width/6)+2 :
                point.play()
                score+=1
                if score%10 == 0 and score < 50:
                    gap_change.play()

        if lives <= 0:
            break
        #change gap size
        
        high_score = max(high_scores)
        lives_text = font.render("Lives: "+str(lives),True,white)
        score_text = font.render("Score: "+str(score),True,white)
        high_score_text = font.render("Best Score: "+str(high_score),True,white)
        screen.blit(score_text,(10,10))
        screen.blit(lives_text,((screen_width/2)-70,10))
        screen.blit(high_score_text,(screen_width-200,10))
        clock.tick(FPS)
        speed1 = FPS
        if score < 50: 
            FPS = 30
            
        elif score >=50 and score <80:
            FPS = 35
            
        elif score >=80 and score <100:
            FPS = 40
            
        elif score >=100 and score <120:
            FPS = 50
            
        else:
            FPS = 55

        speed2 = FPS

        if speed1 != speed2:
            gap_change.play()
        pygame.display.update()
        

    pygame.display.quit()
    high_scores.append(score)
    high_score = max(high_scores)
    print ("Your best score was "+str(high_score))

    save = save()   
    if save == "n":
        pass
    else:    
        
        save_it(high_score)
        
        

    show_scores = raw_input("Show High-Scores?[Y/N]: ")
    scores = sort_it()
    save_new_scores(scores)
    if show_scores == "y":
       
        for item in scores:
            
            print (str(item))
        
    replay = raw_input("Play again?[Y/N]: ")
    if replay == "n":
        quit_it = True
        break

if quit_it == True:
    pygame.quit()
    sys.exit()




    

