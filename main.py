
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys

    import pygame
    from pygame.locals import *

    pygame.init()

    fps = 60
    fpsClock = pygame.time.Clock()

    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    player_color = (0, 255, 0)
    square_size = 10
    land = pygame.image.load("green_square.png")

    land = pygame.transform.scale(land, (square_size, square_size))
    mapsize = 100

    square_list = []


    #global


    global_x = 0
    global_y = 0

    class square:
        def __init__(self, x, y, type):
            self.x = x
            self.y = y
            self.type = type



    class player:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.speed = 10

    p1 = player(width/2, height/2)



    def draw_player():
        pygame.draw.circle(screen, player_color, [p1.x, p1.y], 30, 0)

    def get_input():
        global global_x
        global global_y
        keys_pressed = pygame.key.get_pressed()  # Gets all pressed keys

        if keys_pressed[pygame.K_a] and keys_pressed[
            pygame.K_w]:  # these check if you are trying to move diagonally, and if so reduce your speed to normal (speed/1.41)
            global_x += p1.speed / 1.41
            global_y += p1.speed / 1.41
        elif keys_pressed[pygame.K_a] and keys_pressed[pygame.K_s]:  # A+S
            global_x += p1.speed / 1.41
            global_y -= p1.speed / 1.41
        elif keys_pressed[pygame.K_w] and keys_pressed[pygame.K_d]:  # W+D
            global_y += p1.speed / 1.41
            global_x -= p1.speed / 1.41
        elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_s]:  # D+S
            global_x -= p1.speed / 1.41
            global_y -= p1.speed / 1.41

        else:
            if keys_pressed[pygame.K_a]:  # movement for only one key pressed
                global_x += p1.speed  # Move left

            if keys_pressed[pygame.K_d]:
                global_x -= p1.speed  # Move right

            if keys_pressed[pygame.K_w]:
                global_y += p1.speed  # Move up

            if keys_pressed[pygame.K_s]:
                global_y -= p1.speed  # Move down


    def generate_terrain():
        for x in range(mapsize):
            for y in range(mapsize):
                square_list.append(square(x, y, "land"))


    def display_terrain():
        for square in square_list:

            if square.type == "land":
                screen.blit(land, (square.x*(square_size+1)+global_x, square.y*(square_size+1)+global_y))



    generate_terrain()
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update.

        get_input()

        display_terrain()

        draw_player()
        # Draw.

        pygame.display.flip()
        fpsClock.tick(fps)