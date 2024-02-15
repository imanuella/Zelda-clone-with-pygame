import pygame
import sys
from debug import debug
from settings import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('zeldatest')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        sound_track = pygame.mixer.Sound('project/audio/main.ogg')
        sound_track.set_volume(0.5)
        sound_track.play(loops = -1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            # debug('cyka')
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
