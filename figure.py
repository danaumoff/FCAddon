import pygame
import random
class Figure:
    def __init__(self, screen, x, y):
        # pygame screen
        self.screen = screen

        # figure params
        self.x = x
        self.y = y
        self.hrect = None
        self.color = (128, 128, 128)
        self.loss = 1

        # physics params
        self.x_speed = 0
        self.y_speed = 0
        self.x_boost = 0
        self.y_boost = 0


    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.x_speed += self.x_boost
        self.y_speed += self.y_boost

    def color_change(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def gravity(self, x_boost, y_boost):
        self.x_boost = x_boost
        self.y_boost = y_boost

    def loss_of_speed(self, loss):
        self.loss = loss
    def speed(self, x_speed=-1, y_speed=-1):
        self.x_speed = x_speed
        self.y_speed = y_speed

    def hitbox_collision(self, figure):
        if self.hrect.colliderect((figure.hrect.x, figure.hrect.y, figure.hrect.width, figure.hrect.height)):
            figure.x_speed = -figure.x_speed
            figure.y_speed = -figure.y_speed
            self.x_speed = -self.x_speed
            self.y_speed = -self.y_speed
            for i in range(4):
                self.update()
                figure.update()
            return True
        return False

    def loss_reset_y(self):
        if abs(self.y_speed)*self.loss < 10 * self.y_boost: # 10 - coef
            self.y_speed = 0
            self.x_speed = 0
            self.y_boost = 0

class Block(Figure):

    def __init__(self, screen, x, y, width, height):
        super().__init__(screen, x, y)

        # block params
        self.rect = None
        self.width = width
        self.height = height
        self.border = 250
        self.block_inaccuracy = 0.5

        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)
        self.hrect = self.rect


    def wall_collision(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        if self.x <= 0:
            self.x_speed = -self.x_speed * self.loss
            self.x = self.block_inaccuracy
        if self.y <= 0:
            self.loss_reset_y()
            self.y_speed = -self.y_speed * self.loss
            self.y = self.block_inaccuracy
        if self.x >= screen_width - self.width:
            self.x_speed = -self.x_speed * self.loss
            self.x = screen_width - self.width - self.block_inaccuracy
        if self.y >= screen_height - self.height:
            self.loss_reset_y()
            self.y_speed = -self.y_speed * self.loss
            self.y = screen_height - self.height - self.block_inaccuracy
    def update(self):
        self.rect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)

    def hitbox_update(self):
        super().update()
        self.hrect = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)

class Circle(Figure):

    def __init__(self, screen, x, y, rad):
        super().__init__(screen, x, y)
        self.rad = rad
        self.deg = 0

        self.hrect = pygame.draw.rect(self.screen, self.color, (self.x-self.rad, self.y-self.rad, self.rad*2, self.rad*2), 250)

    def wall_collision(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        if self.x <= self.rad and self.x_speed < 0:
            self.x_speed = -self.x_speed * self.loss
        if self.y <= self.rad and self.y_speed < 0:
            self.loss_reset_y()
            self.y_speed = -self.y_speed * self.loss
        if self.x >= screen_width - self.rad and self.x_speed > 0:
            self.x_speed = -self.x_speed * self.loss
        if self.y >= screen_height - self.rad and self.y_speed > 0:
            self.loss_reset_y()
            self.y_speed = -self.y_speed * self.loss

    def update(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.rad)
    def hitbox_update(self):
        super().update()
        self.hrect = pygame.draw.rect(self.screen, self.color, (self.x-self.rad, self.y-self.rad, self.rad*2, self.rad*2), 250)



