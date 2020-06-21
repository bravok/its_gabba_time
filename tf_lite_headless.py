import pygame

pygame.mixer.init()
pygame.mixer.music.load("yo_gabba_gabba.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()



while pygame.mixer.music.get_busy() == True:
    pass

