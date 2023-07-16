import pygame

from config import (size, font_size, block_size,
                    BLACK, WHITE, LETTERS,
                    left_margin, upper_margin)

pygame.init()

pygame.display.set_caption("Морской Бой")
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('notosans', font_size)


class Grid:
    def __init__(self, title, offset):
        self.title = title
        self.offset = offset
        self.draw_grid()
        self.sign_grids()
        self.add_nums_letters_to_grid()

    def draw_grid(self):
        for i in range(11):
            # Horizontal lines
            x1 = left_margin + self.offset
            y1 = upper_margin + i * block_size
            x2 = left_margin + 10 * block_size + self.offset
            y2 = upper_margin + i * block_size
            pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 1)

            # Vertical lines
            x1 = left_margin + i * block_size + self.offset
            y1 = upper_margin
            x2 = left_margin + i * block_size + self.offset
            y2 = upper_margin + 10 * block_size
            pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 1)

    def add_nums_letters_to_grid(self):
        for i in range(10):
            num_ver = font.render(str(i + 1), True, BLACK)
            letters_hor = font.render(LETTERS[i], True, BLACK)
            num_ver_width = num_ver.get_width()
            num_ver_height = num_ver.get_height()
            letters_hor_width = letters_hor.get_width()

            # Ver num grid1
            x = (left_margin - (block_size // 2 + num_ver_width // 2) +
                 self.offset)
            y = (upper_margin + i * block_size +
                 (block_size // 2 - num_ver_height // 2))
            screen.blit(num_ver, (x, y))

            # Hor letters grid1
            x = (left_margin + i * block_size +
                 (block_size // 2 - letters_hor_width // 2) + self.offset)
            y = upper_margin + 10 * block_size
            screen.blit(letters_hor, (x, y))

    def sign_grids(self):
        player = font.render(self.title, True, BLACK)
        sign_width = player.get_width()
        x = left_margin + 5 * block_size - sign_width // 2 + self.offset
        y = upper_margin - block_size // 2 - font_size
        screen.blit(player, (x, y))


if __name__ == '__main__':

    game_over = False

    screen.fill(WHITE)
    computer_grid = Grid("COMPUTER", 0)
    human_grid = Grid("HUMAN", 15 * block_size)
    # draw_ships(computer.ships)
    # draw_ships(human.ships)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        pygame.display.update()
