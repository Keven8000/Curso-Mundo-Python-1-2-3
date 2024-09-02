import pygame
pygame.init()
pygame.mixer.music.load("Música 1.mp3")
pygame.mixer.music.play()
input('Digite algo para a música para: ')
pygame.event.wait()
