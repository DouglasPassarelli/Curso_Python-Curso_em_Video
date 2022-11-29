# Faça um programa em Python que abra e reproduza um arquivo mp3

import pygame
pygame.init()
pygame.mixer.music.load('ex0021.mp3')
pygame.mixer.music.play()
pygame.event.wait