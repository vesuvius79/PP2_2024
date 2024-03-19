import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("MusicPlayer")


path = [
    "playlist/Travis Scott - Butterfly Effect.mp3",
    "playlist/Travis Scott - Can't Say.mp3",
    "playlist/Travis Scott feat. Drake - Sicko Mode.mp3", 
    "playlist/Travis Scott feat. Swae Lee & Chief Keef - Nightcrawler.mp3",
    "playlist/Travis Scott feat. The Weeknd - Skeletons.mp3",
    "playlist/Michael Jackson - Thriller.mp3",
    "playlist/Michael Jackson - Billie Jean.mp3",
    "playlist/Michael Jackson - Beat it.mp3",
    "playlist/Travis Scott - Apple Pie.mp3",
    "playlist/The Weeknd - After Hours.mp3",
    "playlist/The Weeknd - Earned It.mp3",
    "playlist/The Weeknd - Is There Someone Else.mp3",
    "playlist/The Weeknd - Take My Breath.mp3"
]

current_index = 0
pygame.mixer.music.load(path[current_index])


def play_music():
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def unpause_music():
    pygame.mixer.music.unpause()


def play_next():
    global current_index
    current_index = (current_index + 1) % len(path)
    pygame.mixer.music.load(path[current_index])
    play_music()


def play_previous():
    global current_index
    current_index = (current_index - 1) % len(path)
    pygame.mixer.music.load(path[current_index])
    play_music()


sqaure = pygame.Surface((120, 100))
sqaure.fill("Black")

sqaure0 = pygame.Surface((120, 100))
sqaure0.fill("Black")

running = True
while running:
    
    pygame.draw.circle(screen, "black", (250, 150), 45)
    screen.blit(sqaure, (80, 100))
    screen.blit(sqaure, (300, 100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if pygame.mixer.music.get_busy():
                    pause_music()
                else:
                    unpause_music()
            elif event.key == pygame.K_RIGHT:
                play_next()
            elif event.key == pygame.K_LEFT:
                play_previous()

    screen.fill((255, 255, 255))
    pygame.display.flip()
    

pygame.quit()