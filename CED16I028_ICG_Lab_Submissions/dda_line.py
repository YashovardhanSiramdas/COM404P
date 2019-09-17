import pygame
from pygame import gfxdraw
import sys


x0 = int(input("Enter the value of X0: "))
y0 = int(input("Enter the value of Y0: "))
x1 = int(input("Enter the value of X1: "))
y1 = int(input("Enter the value of Y1: "))

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

size = [700, 700]
screen = pygame.display.set_mode(size)

screen.fill(white)

x = x0
y = y0

for i in range(0,steps+1):
	gfxdraw.pixel(screen, int(x), int(y), black)
	x += Xinc
	y += Yinc
pygame.display.update()

while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()