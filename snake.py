import pygame

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width,height))

block_size = 10
color = (255,255,255)
running = True

for y in range(height):
    for x in range(width):
        rect = pygame.Rect(y * (block_size + 1), x * (block_size + 1), block_size,block_size)
        pygame.draw.rect(screen,color,rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

