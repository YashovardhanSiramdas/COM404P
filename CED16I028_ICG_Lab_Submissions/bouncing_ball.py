import pygame
from pygame import gfxdraw
import sys,time, math

pygame.init()

screen = pygame.display.set_mode((600,480))
running = 1

blue = 0,0,255
white = 255, 255, 255
black = 0,0,0

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0

	screen.fill(black)

	for i in range(20):
		pygame.draw.circle(screen, white, (250,120+(10*i)), 30+i,1)
		pygame.display.update()
		screen.fill(black)
		pygame.time.delay(30)

	for i in range(20):
		pygame.draw.circle(screen, white, (250,250-(10*i)), 45+i,1)
		pygame.display.update()
		screen.fill(black)
		pygame.time.delay(30)

	pygame.time.delay(100)

	for i in range(20):
		pygame.draw.circle(screen, white, (250,120+(10*i)), 60+i,1)
		pygame.display.update()
		screen.fill(black)
		pygame.time.delay(30)

	for i in range(20):
		pygame.draw.circle(screen, white, (250,250-(10*i)), 75+i,1)
		pygame.display.update()
		screen.fill(black)
		pygame.time.delay(30)

	pygame.time.delay(100)

	for i in range(20):
		pygame.draw.circle(screen, white, (250,120+(10*i)), 90+i,1)
		pygame.display.update()
		screen.fill(black)
		pygame.time.delay(30)

	for i in range(20):
		pygame.draw.circle(screen, white, (250,250-(10*i)), 105+i,1)
		pygame.display.update()
		screen.fill(black)
		pygame.time.delay(30)

