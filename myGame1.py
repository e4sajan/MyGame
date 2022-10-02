import pygame
import random
x = pygame.init()

#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


#creating game window
gameWindow = pygame.display.set_mode((700, 600))
pygame.display.set_caption("BABA's First Game")
pygame.display.update()

#game variables
exit_game = False
game_over = False
snk_x = 50
snk_y = 50
vel_x = 0
vel_y = 0
score = 0
fps = 30
snake_size = 10
food_x = random.randint(0, 700)
food_y = random.randint(0, 600)

snk_length = 1
snk_list = []


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

#game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel_x = 5
                vel_y = 0
            if event.key == pygame.K_LEFT:
                vel_x = -5
                vel_y = 0
            if event.key == pygame.K_UP:
                vel_y = -5
                vel_x = 0
            if event.key == pygame.K_DOWN:
                vel_y = 5
                vel_x = 0
    snk_x = snk_x + vel_x
    snk_y = snk_y + vel_y

    head = []
    head.append(snk_x)
    head.append(snk_y)
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    if abs(food_x - snk_x) < 7 and abs(food_y - snk_y) < 7:
        score += 1
        snk_length += 5
        food_x = random.randint(0, 700)
        food_y = random.randint(0, 600)

    gameWindow.fill(white)
    text_screen('SCORE:' + str(score * 10), black, 10, 10)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])
    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()




