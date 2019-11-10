import pygame

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
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

direction = 'down'
while running:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                # move snake up one
                head.move_ip(0,-block_size)
                screen.fill(backgroundcolor)
                pygame.draw.rect(screen,head_color,head)
                direction = 'up'
            elif event.key == 274:
                # move snake down one 
                head = head.move(0,block_size)
                screen.fill(backgroundcolor)
                pygame.draw.rect(screen,head_color,head)
                direction = 'down'
            elif event.key == 275:
                # move snake right one 
                head = head.move(block_size,0)
                screen.fill(backgroundcolor)
                pygame.draw.rect(screen,head_color,head) 
                direction = 'right'
            elif event.key == 276:
                #move snake right one
                head = head.move(-block_size,0)
                screen.fill(backgroundcolor)
                pygame.draw.rect(screen,head_color,head)
                direction = 'left'
        if event.type == pygame.QUIT:
            running = False
    
    if direction == 'right':
        head = head.move(block_size,0)
        screen.fill(backgroundcolor)
        pygame.draw.rect(screen,head_color,head) 
    if direction == 'left':
        head = head.move(-block_size,0)
        screen.fill(backgroundcolor)
        pygame.draw.rect(screen,head_color,head)
    if direction == 'down':
        head = head.move(0,block_size)
        screen.fill(backgroundcolor)
        pygame.draw.rect(screen,head_color,head)
    if direction == 'up':
        head.move_ip(0,-block_size)
        screen.fill(backgroundcolor)
        pygame.draw.rect(screen,head_color,head)

    pygame.display.flip()

