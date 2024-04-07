import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = 5  # Initial speed

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def increase_speed(self):
        self.speed += 1  # Increase speed by 1 unit

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Coin.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = random.choices(range(1, 6), weights=[1, 2, 3, 4, 5])[0] # Random weight between 1 and 5

    def move(self):
        self.rect.move_ip(0, 5)  # Fixed speed for coins
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.coins_collected = 0

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()

collected_points = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()

    if random.randint(1, 100) == 1:
        new_coin = Coin()
        coins.add(new_coin)

    for coin in coins:
        coin.move()

    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    coins.draw(DISPLAYSURF)

    if pygame.sprite.spritecollide(P1, pygame.sprite.Group(E1), False):
        pygame.quit()
        sys.exit()

    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        P1.coins_collected += coin.weight  # Add coin weight to player's collected coins
        collected_points += coin.weight  # Add coin weight to collected points

    if collected_points >= 10:
        E1.increase_speed()
        collected_points -= 10  # Reset collected points after increasing speed

    font = pygame.font.Font(None, 36)
    text = font.render(f"Coins: {P1.coins_collected}", True, BLACK)
    DISPLAYSURF.blit(text, (250, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)
