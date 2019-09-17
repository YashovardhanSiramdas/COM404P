import pygame, random
from pygame import gfxdraw

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

generate_colours = []
colour_filter_array = []

def left_edge():
	# Left edge
	i = 0
	for j in range(0, 7):
		if j == 0:
			r = colour_filter_array[i][j][0]
			g = int((colour_filter_array[i+1][j][1] + colour_filter_array[i][j+1][1])/2)
			b = colour_filter_array[i+1][j+1][2]
			new_colour = (r, g, b)
			pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))
		elif j == 6:
			r = colour_filter_array[i][j][0]
			g = int((colour_filter_array[i+1][j][1] + colour_filter_array[i][j-1][1])/2)
			b = colour_filter_array[i+1][j-1][2]
			new_colour = (r, g, b)
			pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))
		else:
			if j%2 == 0:
				r = colour_filter_array[i][j][0]
				g = int((colour_filter_array[i][j-1][1] + colour_filter_array[i+1][j][1] + colour_filter_array[i][j+1][1])/3)
				b = int((colour_filter_array[i+1][j-1][2] + colour_filter_array[i+1][j+1][2])/2)
				new_colour = (r, g, b)
				pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))
			else:
				r = int((colour_filter_array[i][j-1][0] + colour_filter_array[i][j+1][0])/2)
				g = int((colour_filter_array[i][j][1] + colour_filter_array[i+1][j-1][1] + colour_filter_array[i+1][j+1][1])/3)
				b = colour_filter_array[i+1][j][2]
				new_colour = (r, g, b)
				pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))

def top_edge():
	j = 0
	for i in range(1, 7):
		if i == 6:
			r = colour_filter_array[i][j][0]
			g = int((colour_filter_array[i-1][j][1] + colour_filter_array[i][j+1][1])/2)
			b = colour_filter_array[i-1][j+1][2]
			new_colour = (r, g, b)
			pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))
		else:
			if i%2 == 0:
				r = colour_filter_array[i][j][0]
				g = int((colour_filter_array[i-1][j][1] + colour_filter_array[i+1][j][1] + colour_filter_array[i][j+1][1])/3)
				b = int((colour_filter_array[i-1][j+1][2] + colour_filter_array[i+1][j+1][1])/2)
				new_colour = (r, g, b)
				pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))
			else:
				r = int((colour_filter_array[i-1][j][0] + colour_filter_array[i+1][j][0])/2)
				g = int((colour_filter_array[i][j][1] + colour_filter_array[i-1][j+1][1] + colour_filter_array[i+1][j+1][1])/3)
				b = colour_filter_array[i][j+1][2]
				new_colour = (r, g, b)
				pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))

def right_edge():
	i = 6
	for j in range(1, 7):
		if j == 6:
			r = colour_filter_array[i][j][0]
			g = int((colour_filter_array[i-1][j][1] + colour_filter_array[i][j-1][1])/2)
			b = colour_filter_array[i-1][j-1][2]
			new_colour = (r, g, b)
			pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))
		else:
			if j%2 == 0:
				r = colour_filter_array[i][j][0]
				g = int((colour_filter_array[i][j-1][1] + colour_filter_array[i-1][j][1] + colour_filter_array[i][j+1][1])/3)
				b = int((colour_filter_array[i-1][j-1][2] + colour_filter_array[i-1][j+1][2])/2)
				new_colour = (r, g, b)
				pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))
			else:
				r = int((colour_filter_array[i][j-1][0] + colour_filter_array[i][j+1][0])/2)
				g = int((colour_filter_array[i][j][1] + colour_filter_array[i-1][j-1][1] + colour_filter_array[i-1][j+1][1])/3)
				b = colour_filter_array[i-1][j][2]
				new_colour = (r, g, b)
				pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))

def bottom_edge():
	j = 6
	for i in range(1, 6):
		if i%2 == 0:
			r = colour_filter_array[i][j][0]
			g = int((colour_filter_array[i-1][j][1] + colour_filter_array[i+1][j][1] + colour_filter_array[i][j-1][1])/3)
			b = int((colour_filter_array[i-1][j-1][2] + colour_filter_array[i+1][j-1][2])/2)
		else:
			r = int((colour_filter_array[i-1][j][0] + colour_filter_array[i+1][j][0])/2)
			g = int((colour_filter_array[i][j][1] + colour_filter_array[i-1][j-1][1] + colour_filter_array[i+1][j-1][1])/3)
			b = colour_filter_array[i][j-1][2]
		
		new_colour = (r, g, b)
		pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))

def center_piece():
	for i in range(1, 6):
		for j in range(1, 6):
			if i%2 == 0:
				if j%2 == 0:
					# Red pixel
					r = colour_filter_array[i][j][0]
					g = int((colour_filter_array[i][j-1][1] + colour_filter_array[i][j+1][1] + colour_filter_array[i-1][j][1] + colour_filter_array[i+1][j][1])/4)
					b = int((colour_filter_array[i-1][j-1][2] + colour_filter_array[i+1][j-1][2] + colour_filter_array[i+1][j-1][2] + colour_filter_array[i+1][j+1][2])/4)
				else:
					r = int((colour_filter_array[i][j-1][0] + colour_filter_array[i][j+1][0])/2)
					g = int((colour_filter_array[i][j][1] + colour_filter_array[i-1][j-1][1] + colour_filter_array[i+1][j-1][1] + colour_filter_array[i+1][j-1][1] + colour_filter_array[i+1][j+1][1])/5)
					b = int((colour_filter_array[i-1][j][2] + colour_filter_array[i+1][j][2])/2)

			else:
				if j%2 == 0:
					r = int((colour_filter_array[i-1][j][0] + colour_filter_array[i+1][j][0])/2)
					g = int((colour_filter_array[i][j][1] + colour_filter_array[i-1][j-1][1] + colour_filter_array[i+1][j-1][1] + colour_filter_array[i+1][j-1][1] + colour_filter_array[i+1][j+1][1])/5)
					b = int((colour_filter_array[i][j-1][2] + colour_filter_array[i][j+1][2])/2)
				else:
					r = int((colour_filter_array[i][j-1][0] + colour_filter_array[i][j+1][0] + colour_filter_array[i-1][j][0] + colour_filter_array[i+1][j][0])/4)
					g = int((colour_filter_array[i-1][j][1] + colour_filter_array[i+1][j][1] + colour_filter_array[i][j+1][1] + colour_filter_array[i][j-1][0])/4)
					b = colour_filter_array[i][j][2]
			
			new_colour = (r, g, b)
			pygame.draw.rect(screen, new_colour, pygame.Rect(i*100, j*100, 100, 100))



def apply_filter():	
	left_edge()
	top_edge()
	right_edge()
	bottom_edge()
	center_piece()

def bayers_filter():
	x = 0
	y = 0
	while x < 700:
		y = 0
		generate_colours = []
		while y < 700:
			if (x/100) % 2 == 0:
				if (y/100) % 2 == 0:
					random_colour = (random.randint(0, 255), 0, 0)
					pygame.draw.rect(screen, random_colour, pygame.Rect(x, y, 100, 100))
				else:
					random_colour = (0, random.randint(0, 255), 0)
					pygame.draw.rect(screen, random_colour, pygame.Rect(x, y, 100, 100))
			else:
				if (y/100) % 2 == 0:
					random_colour = (0, random.randint(0, 255), 0)
					pygame.draw.rect(screen, random_colour, pygame.Rect(x, y, 100, 100))
				else:
					random_colour = (0, 0, random.randint(0, 255))
					pygame.draw.rect(screen, random_colour, pygame.Rect(x, y, 100, 100))
			generate_colours.append(random_colour)
			y += 100
		colour_filter_array.append(generate_colours)
		x += 100

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					apply_filter()
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()


if __name__ == "__main__":

	pygame.init()
	size = [700, 700]
	screen = pygame.display.set_mode(size)

	bayers_filter()
	pygame.quit()