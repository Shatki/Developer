import pygame

pygame.init()
for fontname in pygame.font.get_fonts():
    print fontname

screen = pygame.display.set_mode((725,92))
font = pygame.font.SysFont("freeserif", 20 , bold=1)
textSurface = font.render("1 Theremin Per Child", 1,
                          pygame.Color(255, 255, 255))
screen.blit(textSurface, (10, 10))

while True:
    pygame.display.update()