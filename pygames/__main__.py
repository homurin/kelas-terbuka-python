import pygame

# init

pygame.init()

# running game var

is_run = True

# surface object display

wind_length = 500
wind_width = 500

window = pygame.display.set_mode((wind_length, wind_width))

# game object

# coordinate

x = 150
y = 150

# size

length = 20
width = 20

# moving speed

speed = 10


while is_run:
    # delay

    pygame.time.delay(10)

    # user input & database input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False

    # get all keyboard press

    keys = pygame.key.get_pressed()

    # get left

    if (keys[pygame.K_LEFT] and x > 0):
        x -= speed

    # get left

    if (keys[pygame.K_RIGHT] and x < wind_length - length):
        x += speed

    # get down

    if (keys[pygame.K_DOWN] and y < wind_width - width):
        y += speed

    # # get up

    if (keys[pygame.K_UP] and y > 0):
        y -= speed

    # assets update

    window.fill((255, 255, 255))
    pygame.draw.rect(window, (100, 0, 0), (x, y, width, length))

    # display render

    pygame.display.update()

pygame.quit()
