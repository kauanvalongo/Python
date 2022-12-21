import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3.mpeg')
pygame.mixer.music.play()
input()
pygame.event.wait()
