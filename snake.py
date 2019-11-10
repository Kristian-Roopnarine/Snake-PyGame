import pygame

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width,height))

block_size = 10
color = (255,255,255)
head_color = (255,255,0)
running = True

for y in range(height):
    for x in range(width):
        rect = pygame.Rect(y * (block_size + 2), x * (block_size + 2), block_size,block_size)
        pygame.draw.rect(screen,color,rect)

snake = [10,10]
x,y = snake
rect = pygame.Rect(y * (block_size + 2), x * (block_size + 2), block_size,block_size)
pygame.draw.rect(screen,head_color,rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                # move snake up one
                x += block_size
                rect = pygame.Rect(y * (block_size + 2), x * (block_size + 2), block_size,block_size)
                pygame.draw.rect(screen,head_color,rect)
            elif event.key == 274:
                pass
                # move snake down one
            elif event.key == 275:
                pass
                # move snake right one
            elif event.key == 276:
                pass
                #move snake right one
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

