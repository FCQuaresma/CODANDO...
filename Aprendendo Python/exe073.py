import pygame

pygame.init()
pygame.mixer.music.load('Aprendendo Python/exe073a.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()