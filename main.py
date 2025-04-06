import random
import pygame
from Snake import GameLogics


class MainWindow:
    def __init__(self):
        self.WINDOW_X = 720
        self.WINDOW_Y = 480
        self.game_window = None
        self.game = None
        self.current_screen = "menu"
        self.clock = pygame.time.Clock()

    def init_window(self):
        self.game_window = pygame.display.set_mode((self.WINDOW_X, self.WINDOW_Y))
        return self.game_window

    def start_game(self):
        pygame.init()
        pygame.display.set_caption('A snake from a small indie company')
        self.game = GameLogics(self.WINDOW_X, self.WINDOW_Y)
        self.init_window()
        # fps = pygame.time.Clock()  # FPS

    def show_menu(self):
        self.game_window.fill((0, 0, 0))
        font = pygame.font.SysFont('Arial', 50)
        title = font.render('Змейка', True, (255, 255, 255))
        start = font.render('1. Начать игру', True, (255, 255, 255))
        exit_text = font.render('2. Выход', True, (255, 255, 255))

        self.game_window.blit(title, (self.WINDOW_X // 2 - title.get_width() // 2, 100))
        self.game_window.blit(start, (self.WINDOW_X // 2 - start.get_width() // 2, 200))
        self.game_window.blit(exit_text, (self.WINDOW_X // 2 - exit_text.get_width() // 2, 260))
        pygame.display.update()

    def run(self):
        self.start_game()

        while True:
            if self.current_screen == "menu":
                self.show_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.current_screen = "exit"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.current_screen = "game"
                            self.game = GameLogics(self.WINDOW_X, self.WINDOW_Y)
                        elif event.key == pygame.K_2:
                            self.current_screen = "exit"

            elif self.current_screen == "game":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.current_screen = "exit"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.game.change_to = 'UP'
                        if event.key == pygame.K_DOWN:
                            self.game.change_to = 'DOWN'
                        if event.key == pygame.K_LEFT:
                            self.game.change_to = 'LEFT'
                        if event.key == pygame.K_RIGHT:
                            self.game.change_to = 'RIGHT'

                self.game.update_position()

                self.game_window.fill(self.game.map_color)
                self.game.render_snake(self.game_window)
                self.game.render_snake(self.game_window)
                self.game.render_mouse(self.game_window)
                self.game.show_score(self.game_window, self.game.SCORE_COLOR, 'consolas', self.game.SIZE_COLOR)

                self.game.eat_mouse()

                if not self.game.fruit_spawn:
                    self.game.mouse_position = [
                        random.randrange(1, (self.WINDOW_X // 10)) * 10,
                        random.randrange(1, (self.WINDOW_Y // 10)) * 10
                    ]
                    self.game.fruit_spawn = True

                if self.game.suicide() or self.game.snake_translation():
                    self.current_screen = self.game.game_over(self.game_window)

                pygame.display.update()
                self.clock.tick(self.game.snake_speed)

            elif self.current_screen == "exit":
                pygame.quit()
                return


if __name__ == "__main__":
    game = MainWindow()
    game.run()