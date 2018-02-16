import os
import random

BLUE = (0, 0, 250)
GREEN = (0, 250, 0)
RED = (250, 0, 0)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)

class Bird:
    def __init__(self, screen_width, screen_height):
        #inital state
        self.screen_width = screen_width
        self.screen_height = screen_height;
        self.size = (40,40)
        self.speed = 3
        self.x = screen_width / 6
        self.y = screen_height / 2

        self.image = pygame.image.load("Catch-the-pigeon-Here-are-the-best-and-worst-Flappy-Bird-clones.png").convert()
    def jump(self):
        self.speed+=1
    def movement(self):
        self.y += self.speed
        #resets bird
        if self.y <= 0 :
            self.y = 0

        if self.y >= self.screen_height:
            hit.play()
            reset()


    def draw(self):

        self.center = (self.x+20,self.y+20)
        self.image = pygame.transform.smoothscale(self.image,(self.size))
        transparent_color = self.image.get_at((0,0))
        self.image.set_colorkey(transparent_color)
        screen.blit(self.image,(self.x,self.y))


class Wall:
    def __init__(self):
        # initial state
        self.x = game.screen_width
        self.width = 15
        self.top_y = 0
        self.gap_length = 70
        self.top_length = random.randrange(60, game.screen_height - 150)
        self.bottom_y = self.top_length + self.gap_length
        self.bottom_length = game.screen_height - self.bottom_y + 50
        self.image_top = pygame.image.load("Wall_texture_by_stickman_art.jpg")
        self.image_bottom = pygame.image.load("Wall_texture_by_stickman_art.jpg")

    def randomise_wall(self):
        self.top_length = random.randrange(60, game.screen_height - 150)
        self.bottom_y = self.top_length + self.gap_length
        self.bottom_length = game.screen_height - self.bottom_y
        return ()

    def movement(self, score):
        self.x -= 3
        # reset walls
        if self.x < 0 - self.width:
            self.x = game.screen_width
            self.randomise_wall()
        self.bottom_y = self.top_length + self.gap_length
        self.bottom_length = game.screen_height - self.bottom_y

        if score < 10:
            self.gap_length = 100
        elif score < 20:
            self.gap_length = 90
        elif score < 30:
            self.gap_length = 80
        elif score < 40:
            self.gap_length = 70
        elif score < 50:
            self.gap_length = 60
        elif score < 60:
            self.gap_length = 50
        else:
            self.gap_length = 45
        return (score)

    def draw(self):

        self.image_top = pygame.transform.smoothscale(self.image_top, (self.width, self.top_length))
        self.image_bottom = pygame.transform.smoothscale(self.image_bottom, (self.width, self.bottom_length))
        self.top = pygame.draw.rect(screen, GREEN, (self.x, self.top_y, self.width, self.top_length))
        self.bottom = pygame.draw.rect(screen, GREEN, (self.x, self.bottom_y, self.width, self.bottom_length))
        screen.blit(self.image_top, (self.x, self.top_y))
        screen.blit(self.image_bottom, (self.x, self.bottom_y))


def reset():
    global score
    
    score = 0
    bird = Bird()
    wall1.__init__()
    wall2.__init__()
    wall2.x = game.screen_width+(game.screen_width/6)
    wall3.__init__()
    wall3.x = game.screen_width+(2*game.screen_width/6)
    wall4.__init__()
    wall4.x = game.screen_width+(3*game.screen_width/6)
    wall5.__init__()
    wall5.x = game.screen_width+(4*game.screen_width/6)
    wall6.__init__()
    wall6.x = game.screen_width+(5*game.screen_width/6)
    still_screen()

    time.sleep(1)


def save_it(high_score):
    name = input("Name: ")
    fob = open("highscores_flappy_bird.txt","a")
    if high_score < 10:
        fob.write(str(0)+str(high_score)+": "+name+"\n")
    else:    
        fob.write(str(high_score)+": "+name+"\n")
    fob.close()
    print("High score saved in Highscores_flappy_bird.txt")
    return()


def save():
    try:
        save = input("Do you want to save?[Y/N]: ")
    except:
        save()
    return save

def read_it():
    fob = open("highscores_flappy_bird.txt","r")
    scores = fob.readlines()
    return scores


def sort_it():
    scores = read_it()
    scores = sorted(scores,reverse = True)
    return scores


def save_new_scores(scores):
    fob2 = open("highscores_bouncing_ball.txt","w")
    fob2.writelines(scores)
    fob2.close()
    
    return()

def still_screen():
    while True:
        screen.blit(game.background,(0,0))
        game. bird.draw()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return()
        pause_text = font.render("Press SPACE to play",True,WHITE)
        screen.blit(pause_text,((game.screen_width/2)-70,game.screen_height/2))
        scores = sort_it()
        high_score = scores[0]
        high_score = high_score[:-1]
        high_score_text = font.render("High Score - "+str(high_score),True,WHITE)
        screen.blit(high_score_text,((game.screen_width/2)-70,(game.screen_height/2-70)))

        pygame.display.update()
                

class Game:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.walls = []
        self.background = pygame.image.load("video games super mario backgrounds 2560x1024 wallpaper_www.wallmay.net_65.jpg")
        self.set_up_window()
        self.bird = Bird(self.screen_width, self.screen_height)

    def set_up_window(self):
        global screen, background
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (8, 30)  # widnow pop up pos
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("flappy_bird")
        self.background = pygame.transform.smoothscale(self.background, (self.screen_width, self.screen_height))  # resize


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

    game = Game()

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    high_scores = [0]
    score = 0
    lives = 5
    FPS = 30
    gap_length = 75
    score_text = font.render(str(score), True, WHITE)

    #define bird and walls
    #place walls apart

    wall1 = Wall()
    wall2 = Wall()
    wall2.x = game.screen_width+(game.screen_width/6)
    wall3 = Wall()
    wall3.x = game.screen_width+(2*game.screen_width/6)
    wall4 = Wall()
    wall4.x = game.screen_width+(3*game.screen_width/6)
    wall5 = Wall()
    wall5.x = game.screen_width+(4*game.screen_width/6)
    wall6 = Wall()
    wall6.x = game.screen_width+(5*game.screen_width/6)
    #add walls to a list
    game.walls.append(wall1)
    game.walls.append(wall2)
    game.walls.append(wall3)
    game.walls.append(wall4)
    game.walls.append(wall5)
    game.walls.append(wall6)
    
    time.sleep(1)
    pygame.mixer.init()

    still_screen()
        
    

    #animation loop
    while True:
        screen.blit(game.background,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flap.play()
                    #flap - jump up
                    game.bird.speed = -10
        #terminal velocity       
        if game.bird.speed <10:
            #increase falling speed
            game.bird.jump()
        

        game.bird.movement()
        game.bird.draw()
        for item in game.walls:
            item.movement(score)
            item.draw()
            #wall collisions
            if item.top.collidepoint(game.bird.center[0]+5,game.bird.center[1]+5) or item.top.collidepoint(game.bird.center[0]-5,game.bird.center[1]-5) or item.top.collidepoint(game.bird.center[0]+5,game.bird.center[1]-5) or item.top.collidepoint(game.bird.center[0]-5,game.bird.center[1]+5) or item.bottom.collidepoint(game.bird.center[0]+5,game.bird.center[1]+5) or item.bottom.collidepoint(game.bird.center[0]-5,game.bird.center[1]-5) or item.bottom.collidepoint(game.bird.center[0]+5,game.bird.center[1]-5) or item.bottom.collidepoint(game.bird.center[0]-5,game.bird.center[1]+5):
                high_scores.append(score)
                hit.play()
                reset()
                lives -=1
        #wall spacing
        for item in game.walls:
            if item.x == game.screen_width/6 or item.x == (game.screen_width/6)+1 or item.x == (game.screen_width/6)+2 :
                point.play()
                score+=1
                if score%10 == 0 and score < 50:
                    gap_change.play()

        if lives <= 0:
            break
        #change gap size
        
        high_score = max(high_scores)
        lives_text = font.render("Lives: "+str(lives),True,WHITE)
        score_text = font.render("Score: "+str(score),True,WHITE)
        high_score_text = font.render("Best Score: "+str(high_score),True,WHITE)
        screen.blit(score_text,(10,10))
        screen.blit(lives_text,((game.screen_width/2)-70,10))
        screen.blit(high_score_text,(game.screen_width-200,10))
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
        
        

    show_scores = input("Show High-Scores?[Y/N]: ")
    scores = sort_it()
    save_new_scores(scores)
    if show_scores == "y":
       
        for item in scores:
            
            print (str(item))
        
    replay = input("Play again?[Y/N]: ")
    if replay == "n":
        quit_it = True
        break

if quit_it == True:
    pygame.quit()
    sys.exit()




    

