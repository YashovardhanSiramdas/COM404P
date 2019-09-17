import pygame
from pygame import gfxdraw

black = (0, 0, 0)
white = (255, 255, 255)

def plot_line_low(x0, y0, x1, y1, dx, dy):
	y = y0
	DV = dx - 2*dy

	for x in range(x0, x1+1):
		print(x, y)
		gfxdraw.pixel(screen, int(round(x)), int(round(y)), black)

		if DV >= 0:
			DV -= 2*dy
		else:
			y += 1
			DV -= 2*(dy - dx)

def plot_line_high(x0, y0, x1, y1, dx, dy):
	x = x0
	DV = dx - 2*dy

	for y in range(y0, y1+1):
		gfxdraw.pixel(screen, int(round(x)), int(round(y)), black)

		if DV >= 0:
			DV -= 2*dy
		else:
			x += 1
			DV -= 2*(dy - dx)

def plot_same_slope(x0, y0, x1, y1):
	y = y0
	x = x0
	for x in range(x0, x1):
		gfxdraw.pixel(screen, int(round(x)), int(round(y)), black)
		y -= 1

def bresenham_line(initial_point, final_point):
	screen.fill(white)
	dx = final_point[0] - initial_point[0]
	dy = final_point[1] - initial_point[1]

	if abs(dy) == abs(dx):
		if initial_point[0] < final_point[1]:
			plot_same_slope(initial_point[0], initial_point[1], final_point[0], final_point[1])
		else:
			plot_same_slope(final_point[0], final_point[1], initial_point[0], initial_point[1])
	elif abs(dy) < abs(dx):
		if initial_point[0] < final_point[0]:
			plot_line_low(initial_point[0], initial_point[1], final_point[0], final_point[1], dx, dy)
		else:
			plot_line_low(final_point[0], final_point[1], initial_point[0], initial_point[1], (-1)*dx, (-1)*dy)
	else:
		if initial_point[1] < final_point[1]:
			plot_line_high(initial_point[0], initial_point[1], final_point[0], final_point[1], dx, dy)
		else:
			plot_line_low(final_point[0], final_point[1], initial_point[0], initial_point[1], (-1)*dx, (-1)*dy)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()


if __name__ == "__main__":
	initial_point = input("Enter the x1,y1 point: ")
	final_point = input("Enter the x2,y2 point: ")

	initial_point = [int(x) for x in initial_point.split(',')]
	final_point = [int(x) for x in final_point.split(',')]

	pygame.init()
	size = [700, 500]
	screen = pygame.display.set_mode(size)

	bresenham_line(initial_point, final_point)
	pygame.quit()