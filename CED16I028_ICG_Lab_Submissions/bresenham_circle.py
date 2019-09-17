import pygame
from pygame import gfxdraw

black = (0, 0, 0)
white = (255, 255, 255)

def plot_circle(center_x, center_y, offset_x, offset_y):
	gfxdraw.pixel(screen, int(center_x + offset_x), int(center_y + offset_y), black)
	gfxdraw.pixel(screen, int(center_x - offset_x), int(center_y + offset_y), black)
	gfxdraw.pixel(screen, int(center_x + offset_x), int(center_y - offset_y), black)
	gfxdraw.pixel(screen, int(center_x - offset_x), int(center_y - offset_y), black)
	gfxdraw.pixel(screen, int(center_x + offset_y), int(center_y + offset_x), black)
	gfxdraw.pixel(screen, int(center_x - offset_y), int(center_y + offset_x), black)
	gfxdraw.pixel(screen, int(center_x + offset_y), int(center_y - offset_x), black)
	gfxdraw.pixel(screen, int(center_x - offset_y), int(center_y - offset_x), black)

def bresenham_circle(center, radius):
	screen.fill(white)
	new_x = 0
	new_y = radius
	DV = 3 - 2*radius

	while new_y >= new_x:
		new_x += 1

		if DV > 0:
			new_y -= 1
			DV += 4*(new_x - new_y) + 10;
		else:
			DV += 4*new_x + 6

		plot_circle(center[0], center[1], new_x, new_y)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()


if __name__ == "__main__":
	center = input("Enter the center point: ")
	radius = float(input("Enter radius: "))

	center = [float(x) for x in center.split(',')]

	pygame.init()
	size = [700, 500]
	screen = pygame.display.set_mode(size)

	bresenham_circle(center, radius)
	pygame.quit()