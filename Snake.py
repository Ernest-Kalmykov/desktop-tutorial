import pygame
import time
import random

from main import MainWindow


# Так как у меня проблемы с классами, их нет будет. Просто глобальные переменные

class GameLogics:
    MOUSE_COLOR = pygame.Color(255, 255, 255)
    LOSING_LABEL_COLOR = pygame.Color(255, 0, 0)
    SIZE_COLOR = 20


    def __init__(self):
        self.snake_speed = 15
        self.map_color = pygame.Color(0, 0, 0)
        self.color_snake = pygame.Color(0, 255, 0)
        self.snake_position = [100, 50]
        self.SCORE_COLOR = pygame.Color(255, 255, 255)
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.mouse_position = [random.randrange(1, (MainWindow().WINDOW_X // 10)) * 10,
                          random.randrange(1, (MainWindow().WINDOW_Y // 10)) * 10]
        self.fruit_spawn = True
        self.score = 0
        self.direction = 'RIGHT'

    def show_score(self, color, font, size):
        color = self.SCORE_COLOR# Функция счёта
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Счёт: ' + str(self.score), True, color)
        MainWindow().init_window().blit(score_surface, (10, 10))

    def game_over(self):  # Функция завершения игры
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Игра окончена Счёт: ' + str(self.score), True, GameLogics.LOSING_LABEL_COLOR)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (MainWindow().WINDOW_X/ 2, MainWindow().WINDOW_Y / 4)
        MainWindow().init_window().blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    def body_enlargement(self):
        self.snake_body.insert(0, list(self.snake_position))  # Как змея ест мышей

    def eat_mouse(self):
        self.body_enlargement()
        if self.snake_position[0] == self.mouse_position[0] and self.snake_position[1] == self.mouse_position[1]:
            self.score += 10
            self.fruit_spawn = False
        else:
            self.snake_body.pop()

    def render_snake(self):
        for pos in self.snake_body:
            pygame.draw.rect(MainWindow().init_window(), self.color_snake, pygame.Rect(pos[0], pos[1], 10, 10))

    def render_mouse(self):
        pygame.draw.rect(MainWindow().init_window(), self.SCORE_COLOR, pygame.Rect(self.mouse_position[0], self.mouse_position[1], 10, 10))

    # TODO В будущем сделать перевод змеи через концы экрана (должно зависить от сложности)
    def snake_translation(self):
        if self.snake_position[0] < 0 or self.snake_position[0] > MainWindow().WINDOW_X - 10:
            self.game_over()
        if self.snake_position[1] < 0 or self.snake_position[1] > MainWindow().WINDOW_Y - 10:
            self.game_over()

    def suicide(self):
        for block in self.snake_body[1:]:
            if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                self.game_over()

# window_x = 720
# window_y = 480
#black = pygame.Color(0, 0, 0)
#white = pygame.Color(255, 255, 255)
#red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)
# pygame.init()
# pygame.display.set_caption('A snake from a small indie company')
# game_window = pygame.display.set_mode((window_x, window_y))
# fps = pygame.time.Clock()  # FPS

# Начальные параметры змейки

#fruit_spawn = True
#direction = 'RIGHT'
#change_to = direction
#score = 0
# def show_score(color, font, size):  # Функция счёта
#     score_font = pygame.font.SysFont(font, size)
#     score_surface = score_font.render('Счёт: ' + str(score), True, color)
#     game_window.blit(score_surface, (10, 10))
# def game_over():    # Функция завершения игры
#     my_font = pygame.font.SysFont('times new roman', 50)
#     game_over_surface = my_font.render('Игра окончена Счёт: ' + str(score), True, red)
#     game_over_rect = game_over_surface.get_rect()
#     game_over_rect.midtop = (window_x / 2, window_y / 4)
#     game_window.blit(game_over_surface, game_over_rect)
#     pygame.display.flip()
#     time.sleep(2)
#     pygame.quit()
#     quit()
# while True:
#     for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_UP:
    #             change_to = 'UP'
    #         if event.key == pygame.K_DOWN:
    #             change_to = 'DOWN'
    #         if event.key == pygame.K_LEFT:
    #             change_to = 'LEFT'
    #         if event.key == pygame.K_RIGHT:
    #             change_to = 'RIGHT'
    # if change_to == 'UP' and direction != 'DOWN':   # Запрещаю поворачивать в противоположную сторону
    #     direction = 'UP'
    # if change_to == 'DOWN' and direction != 'UP':
    #     direction = 'DOWN'
    # if change_to == 'LEFT' and direction != 'RIGHT':
    #     direction = 'LEFT'
    # if change_to == 'RIGHT' and direction != 'LEFT':
    #     direction = 'RIGHT'
    # if direction == 'UP':
    #     snake_position[1] -= 10
    # if direction == 'DOWN':
    #     snake_position[1] += 10
    # if direction == 'LEFT':
    #     snake_position[0] -= 10
    # if direction == 'RIGHT':
    #     snake_position[0] += 10



    # if not fruit_spawn:
    #     mouse_position = [random.randrange(1, (window_x // 10)) * 10,
    #                       random.randrange(1, (window_y // 10)) * 10]
    # fruit_spawn = True

    # TODO ХЗ ПОКА КАК СДЕЛАТЬ game_window.fill(black)

    # for pos in snake_body:
    #     pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # pygame.draw.rect(game_window, white, pygame.Rect(mouse_position[0], mouse_position[1], 10, 10))

    # if snake_position[0] < 0 or snake_position[0] > window_x - 10:
    #     game_over()
    # if snake_position[1] < 0 or snake_position[1] > window_y - 10:
    #     game_over()

    # for block in snake_body[1:]:
    #     if snake_position[0] == block[0] and snake_position[1] == block[1]:
    #         game_over()

    # show_score(white, 'consolas', 20)
    # pygame.display.update()
    # fps.tick(snake_speed)