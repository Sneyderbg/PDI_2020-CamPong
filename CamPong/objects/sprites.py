import pygame
from pygame import *
from math import sqrt, fabs


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.rect = Rect(x, y, width, height)
        self.Vx, self.Vy = 1, 1
        self.direction_x = 1
        self.V = sqrt(self.Vx ** 2 + self.Vy ** 2)

    def move(self):
        self.rect.move_ip(self.Vx * self.direction_x, self.Vy)

    def set_speed(self, speed):
        sin = self.Vx / self.V
        cos = self.Vy / self.V
        self.V = speed
        self.Vx, self.Vy = sin * self.V, cos * self.V

    def set_speed_xy(self, speed_x, speed_y):
        self.Vx, self.Vy = speed_x, speed_y
        self.V = sqrt(self.Vx ** 2 + self.Vy ** 2)

    def set_direction(self, direction):
        assert isinstance(direction, int)
        assert direction in (-1, 1), "param \'direction\' must be 1 or -1"
        self.direction_x = direction

    def set_xy(self, x, y):
        self.rect.x, self.rect.y = x, y


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color=(0, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.rect = Rect(x, y, width, height)
        self.speed = 2

    def move(self, direction):
        assert direction in ('up', 'down'), "param \'direction\' must be up/down"
        if direction == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def set_speed(self, speed):
        self.speed = speed

    def set_xy(self, x, y):
        self.rect.x, self.rect.y = x, y
