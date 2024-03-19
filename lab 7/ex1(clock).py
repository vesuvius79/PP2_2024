import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((1000, 800))
window_title = pygame.display.set_caption("mickeyclock")
clock = pygame.time.Clock()
FPS = 60
clock_skelet = pygame.image.load("images/main-clock.png")
left_hand = pygame.image.load("images/left-hand.png")
right_hand = pygame.image.load("images/right-hand.png")
clock_skelet_rect = clock_skelet.get_rect(center=(500, 400))

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    now = datetime.now().time()

    seconds_angle = -(now.second * 6 - 84)
    minutes_angle = -(now.minute * 6 - 90)

    rotated_left_hand = pygame.transform.rotate(left_hand, seconds_angle)
    rotated_right_hand = pygame.transform.rotate(right_hand, minutes_angle)

    left_hand_rect = rotated_left_hand.get_rect(center=clock_skelet_rect.center)
    right_hand_rect = rotated_right_hand.get_rect(center=clock_skelet_rect.center)

    screen.blit(clock_skelet, clock_skelet_rect)
    screen.blit(rotated_left_hand, left_hand_rect)
    screen.blit(rotated_right_hand, right_hand_rect)

    pygame.display.flip()
    clock.tick(FPS)
