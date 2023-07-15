import pygame

from config import size, font_size, BLACK, left_margin, upper_margin, block_size


class Field:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Морской Бой")
        self.screen = pygame.display.set_mode(size)
        self.font = pygame.font.SysFont('notosans', font_size)


class Grid(Field):
    def __init__(self, title, offset):
        self.title = title
        self.offset = offset
        self.draw_grid()
        self.sign_grids()
        self.add_nums_letters_to_grid()

    def draw_grid(self):
        for i in range(11):
            # Horizontal lines
            pygame.draw.line(self.screen, BLACK, (left_margin+self.offset, upper_margin+i*block_size),
                            (left_margin+10*block_size+self.offset, upper_margin+i*block_size), 1)
            # Vertical lines
            pygame.draw.line(self.screen, BLACK, (left_margin+i*block_size+self.offset, upper_margin),
                            (left_margin+i*block_size+self.offset, upper_margin+10*block_size), 1)

    def add_nums_letters_to_grid(self):
        for i in range(10):
            num_ver = self.font.render(str(i+1), True, BLACK)
            letters_hor = self.font.render(LETTERS[i], True, BLACK)
            num_ver_width = num_ver.get_width()
            num_ver_height = num_ver.get_height()
            letters_hor_width = letters_hor.get_width()

            # Ver num grid1
            self.screen.blit(num_ver, (left_margin - (block_size//2+num_ver_width//2)+self.offset,
                                    upper_margin + i*block_size + (block_size//2 - num_ver_height//2)))
            # Hor letters grid1
            self.screen.blit(letters_hor, (left_margin + i*block_size + (block_size //
                                                                    2 - letters_hor_width//2)+self.offset, upper_margin + 10*block_size))

    def sign_grids(self):
        player = self.font.render(self.title, True, BLACK)
        sign_width = player.get_width()
        self.screen.blit(player, (left_margin + 5*block_size - sign_width //
                            2+self.offset, upper_margin - block_size//2 - font_size))
