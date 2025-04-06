import random

import pygame

from Snake import GameLogics


GAME_RUNNING = True

class MainWindow(GameLogics):
    def __init__(self):
        super().__init__()
        self.WINDOW_X = 720
        self.WINDOW_Y = 480


    def init_window(self):
        game_window = pygame.display.set_mode((self.WINDOW_X, self.WINDOW_Y))

    def start_game(self):
        pygame.init()
        pygame.display.set_caption('A snake from a small indie company')
        self.init_window()
        # fps = pygame.time.Clock()  # FPS

    def change_snake_direction(self):
        change_to = GameLogics().direction

    def clear_screen(self):
        self.init_window().fill(GameLogics().map_color)

if __name__ == "main":
    while GAME_RUNNING:
        main_window = MainWindow()
        main_window.start_game()

        fps = pygame.time.Clock()  # FPS

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
            if main_window.change_snake_direction() == 'UP' and main_window.change_snake_direction() != 'DOWN':  # Запрещаю поворачивать в противоположную сторону
                direction = 'UP'
            if main_window.change_snake_direction() == 'DOWN' and main_window.change_snake_direction() != 'UP':
                direction = 'DOWN'
            if main_window.change_snake_direction() == 'LEFT' and main_window.change_snake_direction() != 'RIGHT':
                direction = 'LEFT'
            if main_window.change_snake_direction() == 'RIGHT' and main_window.change_snake_direction() != 'LEFT':
                direction = 'RIGHT'
            if main_window.change_snake_direction() == 'UP':
                GameLogics().snake_position[1] -= 10
            if main_window.change_snake_direction() == 'DOWN':
                GameLogics().snake_position[1] += 10
            if main_window.change_snake_direction() == 'LEFT':
                GameLogics().snake_position[0] -= 10
            if main_window.change_snake_direction() == 'RIGHT':
                GameLogics().snake_position[0] += 10

            if event.type == pygame.QUIT:
                GAME_RUNNING = False

            if not GameLogics().fruit_spawn:
                mouse_position = [random.randrange(1, (main_window.WINDOW_X // 10)) * 10,
                                  random.randrange(1, (main_window.WINDOW_Y // 10)) * 10]
            fruit_spawn = True

        GameLogics().show_score(GameLogics().SCORE_COLOR, 'consolas', GameLogics.SIZE_COLOR)
        pygame.display.update()
        fps.tick(GameLogics().snake_speed)

    else:
        quit()
