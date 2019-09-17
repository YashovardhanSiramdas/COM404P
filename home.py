import pygame
from pygame import gfxdraw
import sys


x0 = 500
y0 = 
x1 = 
y1 = 

dx = abs(x1-x0)
dy = abs(y1-y0)

if abs(dx) > abs(dy):
	steps = abs(dx)
else:
	steps = abs(dy)

Xinc = dx / steps
Yinc = dy / steps

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

size = [1440, 900]
screen = pygame.display.set_mode(size)

screen.fill(white)

x = x0
y = y0

for i in range(0,steps+1):
	gfxdraw.pixel(screen, int(x), int(y), black)
	pygame.display.update()
	x += Xinc
	y += Yinc

while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()