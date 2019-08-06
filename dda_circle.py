import pygame
from pygame import gfxdraw
import sys


xc = int(input("Enter the value of X0: "))
yc = int(input("Enter the value of Y0: "))

r = int(input("Enter the value of radius: "))

xc1 = float(r)
yc1 = float(0)
sx = xc1
sy = yc1

i = 0

while True:
	val = pow(2,i)
	print ("value: ")
	print (val)
	i += 1
	if not val<r:
		break

eps = 1/pow(2,i-1)
print (eps)

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

size = [1440, 900]
screen = pygame.display.set_mode(size)

screen.fill(white)

while True:
	xc2 = xc1 + yc1 * eps
	yc2 = yc1 - eps * xc2

	gfxdraw.pixel(screen, int(xc+xc2), int(yc-yc2), black)

	xc1 = xc2
	yc1 = yc2

	if not ((yc1-sy)<eps or (sx-xc1)>eps):
		pygame.display.update()
		break

while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()