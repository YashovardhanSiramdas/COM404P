import pygame, math
from pygame import gfxdraw

black = (0, 0, 0)
white = (255, 255, 255)

def levy_C_Curve(initial_X, initial_Y, length, alpha, iterations):
	if iterations > 0 :
		length = float(length/math.sqrt(2))
		levy_C_Curve(initial_X, initial_Y, length, alpha + 45, iterations - 1)
		levy_C_Curve((initial_X + length * math.cos(math.radians (45 + alpha))),
						 (initial_Y + length * math.sin(math.radians (45 + alpha))),
						 length, alpha - 45, iterations - 1)
	else :
		endX = int(initial_X + (length * math.cos(math.radians(alpha))))
		endY = int(initial_Y + (length * math.sin(math.radians(alpha))))
		pygame.draw.line(screen, black, [initial_X, initial_Y], [endX, endY], 1)
		pygame.display.update()

def draw_levy(initial_X, initial_Y, iterations, length):
	levy_C_Curve(initial_X, initial_Y, int(length), 0, int(iterations))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()


if __name__ == "__main__":
	initial_point = input("Enter the starting point: ")
	initial_point = [int(x) for x in initial_point.split(',')]

	iterations = input("Enter the number of iterations: ")
	length = input("Enter the length: ")

	pygame.init()
	size = [700, 700]
	screen = pygame.display.set_mode(size)
	screen.fill(white)

	draw_levy(initial_point[0], initial_point[1], iterations, length)
	pygame.quit()