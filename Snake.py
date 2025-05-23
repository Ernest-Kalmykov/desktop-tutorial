import pygame
import time
import random


class GameLogics:
    MOUSE_COLOR = pygame.Color(255, 255, 255)
    LOSING_LABEL_COLOR = pygame.Color(255, 0, 0)
    SIZE_COLOR = 20


    def __init__(self, window_x, window_y):
        self.snake_speed = 15
        self.map_color = pygame.Color(111, 110, 10)
        self.color_snake = pygame.Color(0, 255, 0)
        self.snake_position = [100, 50]
        self.SCORE_COLOR = pygame.Color(255, 255, 255)
        #self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.window_x = window_x
        self.window_y = window_y
        self.mouse_position = [
            random.randrange(1, (self.window_x // 10)) * 10,
                               random.randrange(1, (self.window_y // 10)) * 10
        ]
        self.fruit_spawn = True
        self.score = 0
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def show_score(self, window, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Счёт: ' + str(self.score), True, color)
        window.blit(score_surface, (10, 10))

    def game_over(self, window):  # Функция завершения игры
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Игра окончена Счёт: ' + str(self.score), True, self.LOSING_LABEL_COLOR)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.window_x / 2, self.window_y / 4)
        window.blit(game_over_surface, game_over_rect)
        pygame.display.update()
        time.sleep(2)
        return "menu"

    # Увеличение размера змеи
    def body_enlargement(self):
        #self.snake_body.insert(0, list(self.snake_position))  # Как змея ест мышей
        new_segment_body = [100, 50]
        self.snake_body.append(new_segment_body)

    def eat_mouse(self):
        if (self.snake_position[0] == self.mouse_position[0] and self.snake_position[1] == self.mouse_position[1]):
            self.score += 10
            self.fruit_spawn = False
            self.body_enlargement()

    def render_snake(self, window):
        for pos in self.snake_body:
            pygame.draw.rect(window, self.color_snake, pygame.Rect(pos[0], pos[1], 10, 10))

    def render_mouse(self, window):
        pygame.draw.rect(window, self.MOUSE_COLOR, pygame.Rect(self.mouse_position[0], self.mouse_position[1], 10, 10))

    # TODO В будущем сделать перевод змеи через концы экрана (должно зависить от сложности)
    def snake_translation(self):
        if self.snake_position[0] < 0 or self.snake_position[0] > self.window_x - 10:
            return True
        if self.snake_position[1] < 0 or self.snake_position[1] > self.window_y - 10:
            return True
        return False

    def suicide(self):
        for block in self.snake_body[1:]:
            if self.snake_position[0] == block[0] and self.snake_position[1] == block[1]:
                return True
        return False

    def update_position(self):
        if self.change_to == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.change_to == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        if self.change_to == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.change_to == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

        if self.direction == "UP":
            self.snake_position[1] -= 10
        if self.direction == "DOWN":
            self.snake_position[1] += 10
        if self.direction == "LEFT":
            self.snake_position[0] -= 10
        if self.direction == "RIGHT":
            self.snake_position[0] += 10

        self.snake_body.insert(0, list(self.snake_position))
        if self.snake_body:
            self.snake_body.pop()