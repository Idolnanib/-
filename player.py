from settings import *
import pygame

class Player:
    def __init__(self):
        self.x, self.y = player_pos

        #print(self.x, self.y, type(self.x), type(self.y))
        self.angle = player_angle


    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= player_speed
        if keys[pygame.K_s]:
            self.y += player_speed
        if keys[pygame.K_a]:
            self.x -= player_speed
        if keys[pygame.K_d]:
            self.x += player_speed
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02