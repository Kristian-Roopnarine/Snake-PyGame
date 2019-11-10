import pygame

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width,height))

block_size = 10
backgroundcolor = (0,0,0)
head_color = (255,0,0)
running = True

for y in range(height//10 + 10):
    for x in range(width//10 + 10):
        rect = pygame.Rect(y * (block_size), x * (block_size), block_size,block_size)
        pygame.draw.rect(screen,backgroundcolor,rect)

snake = [10,10]
x,y = snake
head = pygame.Rect(y ,x, block_size,block_size)
pygame.draw.rect(screen,head_color,head)

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                # move snake up one
                head = head.move(0,-block_size)
                pygame.draw.rect(screen,head_color,head)
            elif event.key == 274:
                # move snake down one 
                head = head.move(0,block_size)
                pygame.draw.rect(screen,head_color,head)
            elif event.key == 275:
                # move snake right one 
                head = head.move(block_size,0)
                pygame.draw.rect(screen,head_color,head) 
            elif event.key == 276:
                #move snake right one
                head = head.move(-block_size,0)
                pygame.draw.rect(screen,head_color,head)
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

