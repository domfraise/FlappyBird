import random

import pygame

from Flappy_circle import screen_width, screen_height, screen, green


class Wall():
    def __init__(self):
        #initial state
        self.x = screen_width
        self.width = 15
        self.top_y = 0
        self.gap_length = 70
        self.top_length = random.randrange(60,screen_height-150)
        self.bottom_y = self.top_length + self.gap_length
        self.bottom_length = screen_height - self.bottom_y+50
        self.image_top = pygame.image.load("Wall_texture_by_stickman_art.jpg")
        self.image_bottom = pygame.image.load("Wall_texture_by_stickman_art.jpg")
    def randomise_wall(self):
        self.top_length = random.randrange(60,screen_height-150)
        self.bottom_y = self.top_length + self.gap_length
        self.bottom_length = screen_height - self.bottom_y
        return()

    def movement(self,score):
        self.x -= 3
        #reset walls
        if self.x < 0-self.width:
            self.x = screen_width
            self.randomise_wall()
        self.bottom_y = self.top_length + self.gap_length
        self.bottom_length = screen_height - self.bottom_y

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

        self.image_top = pygame.transform.smoothscale(self.image_top,(self.width,self.top_length))
        self.image_bottom = pygame.transform.smoothscale(self.image_bottom,(self.width,self.bottom_length))
        self.top = pygame.draw.rect(screen,green,(self.x,self.top_y,self.width,self.top_length))
        self.bottom = pygame.draw.rect(screen,green,(self.x,self.bottom_y,self.width,self.bottom_length))
        screen.blit(self.image_top,(self.x,self.top_y))
        screen.blit(self.image_bottom,(self.x,self.bottom_y))