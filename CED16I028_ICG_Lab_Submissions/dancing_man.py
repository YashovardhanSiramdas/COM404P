import pygame, math, time, sys
from pygame import gfxdraw

black = (0, 0, 0)
white = (255, 255, 255)
blue = (52, 137, 235)

def draw_body1(hands_direction="down"):
	pygame.draw.circle(screen, black, (350, 200), 30)
	pygame.draw.line(screen, black, (350, 230), (370, 300))
	pygame.draw.line(screen, black, (370, 300), (330, 360))
	pygame.draw.line(screen, black, (370, 300), (365, 360))

	if hands_direction == "down":
		pygame.draw.line(screen, black, (350, 230), (320, 280))
		pygame.draw.line(screen, black, (350, 230), (345, 280))
	else:
		pygame.draw.line(screen, black, (350, 230), (280, 220))
		pygame.draw.line(screen, black, (350, 230), (290, 180))

def draw_body2(hands_direction="down"):
	pygame.draw.circle(screen, black, (350, 200), 30)
	pygame.draw.line(screen, black, (350, 230), (340, 300))
	pygame.draw.line(screen, black, (340, 300), (350, 360))
	pygame.draw.line(screen, black, (340, 300), (385, 360))

	if hands_direction == "down":
		pygame.draw.line(screen, black, (350, 230), (385, 280))
		pygame.draw.line(screen, black, (350, 230), (360, 280))
	else:
		pygame.draw.line(screen, black, (350, 230), (420, 220))
		pygame.draw.line(screen, black, (350, 230), (410, 180))

def change_man(flag):
	if flag == 0:
		draw_body1()
	elif flag == 1:
		draw_body2()
	elif flag == 2:
		draw_body2("up")
	elif flag == 3:
		draw_body1("up")

	pygame.display.update()

def dancing_man():
	flag = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		change_man(flag)
		pygame.time.delay(500)
		screen.blit(background, (0, 0))
		screen.fill(blue)

		flag += 1
		if flag == 4:
			flag = 0

pygame.init()
size = [700, 700]
background = pygame.Surface(size)
screen = pygame.display.set_mode(size)
screen.fill(blue)

dancing_man()
pygame.quit()