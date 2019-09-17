import pygame
from pygame import gfxdraw
import math
import sys

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 700]
screen = pygame.display.set_mode(size) #Opens a window of size 700,500, and stores it in a variable called screen
screen.fill(white)

pygame.draw.rect(screen,black,(200,300,300,200),1) #House
pygame.draw.polygon(screen, black, [[170, 300], [530, 300],[350, 200]], 1) #Triangle
pygame.draw.rect(screen,black,(275,485,150,15),1) #step 0
pygame.draw.rect(screen,black,(275,475,150,10),1) #step 1
pygame.draw.rect(screen,black,(305,355,90,120),1) #door
pygame.draw.rect(screen,black,(220,355,60,60),1) #window left
pygame.draw.rect(screen,black,(420,355,60,60),1) #window right
pygame.draw.line(screen, black, (220, 385), (280, 385)) #horizontal line window left
pygame.draw.line(screen, black, (420, 385), (480, 385)) #horizontal line window right
pygame.draw.line(screen, black, (250, 385), (250, 415)) #vertical line window left
pygame.draw.line(screen, black, (450, 385), (450, 415)) #vertical line window right
pygame.draw.circle(screen, black, (315,415), 5,1) #Door handle
pygame.display.update() #nothing is drawn


while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()