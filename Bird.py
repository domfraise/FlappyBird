import pygame

from Flappy_circle import screen_width, screen_height, hit, reset, screen


class Bird():
    def __init__(self):
        #inital state
        self.size = (40,40)
        self.speed = 3
        self.x = screen_width/6
        self.y = screen_height/2

        self.image = pygame.image.load("Catch-the-pigeon-Here-are-the-best-and-worst-Flappy-Bird-clones.png").convert()
    def jump(self):
        self.speed+=1
    def movement(self):
        self.y += self.speed
        #resets bird
        if self.y <= 0 :
            self.y = 0

        if self.y >= screen_height:
            hit.play()
            reset()


    def draw(self):

        self.center = (self.x+20,self.y+20)
        self.image = pygame.transform.smoothscale(self.image,(self.size))
        transparent_color = self.image.get_at((0,0))
        self.image.set_colorkey(transparent_color)
        screen.blit(self.image,(self.x,self.y))