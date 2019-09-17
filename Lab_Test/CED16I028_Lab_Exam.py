import pygame
from pygame import gfxdraw
import math
import sys

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
size = [1400, 1200]
screen = pygame.display.set_mode(size) 
screen.fill(white)

pygame.draw.ellipse(screen, black, (250,250,300,180),1)
pygame.draw.ellipse(screen, black, (300,300,150,80),1)
pygame.draw.ellipse(screen, black, (200,200,500,280),1)
pygame.draw.ellipse(screen, black, (170,170,600,340),1)
pygame.draw.ellipse(screen, black, (150,150,700,380),1)

pygame.draw.ellipse(screen, black, (130,130,800,420),1)
pygame.draw.ellipse(screen, black, (110,110,900,460),1)
pygame.draw.ellipse(screen, black, (90,90,1000,500),1)
pygame.draw.ellipse(screen, black, (70,70,1100,540),1)
pygame.draw.ellipse(screen, black, (50,50,1200,580),1)


pygame.display.update()


while True:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()