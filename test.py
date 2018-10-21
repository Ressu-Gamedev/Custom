
import pygame as pg
import random
from settings import *
from sprites import *
from os import path


class Game:

    def __init__(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT)
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        # load sounds
        self.sound_dir = path.join(self.dir, 'sounds')
        # sound effects will be added below

    def run(self):
        pg.mixer.music.play(loops = -1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            generateCannon(100,100)
        pg.mixer.music.fadeout(500)

    def reset(self):
        pg.mixer.music.load(path.join(self.sound_dir, 'loop1.wav'))
        self.run()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(WHITE)
        pg.display.flip()

    def start_screen(self):
        self.screen.fill(BLUE)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("- Orbs will be launched out of a cannon", 24, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("- You must make sure that they arrive at their destination", 24, WHITE, WIDTH / 2, HEIGHT / 2 - 24)
        self.draw_text("- Watch out, theres a time limit!", 24, WHITE, WIDTH / 2, HEIGHT / 2 - 48)
        self.draw_text("Press any key to play, you gopnik", 24, WHITE, WIDTH / 2, HEIGHT / 2 - 72)
        pg.display.flip()
        self.wait_for_key()

    def end_screen(self):
        if not self.running:
            return
        self.screen.fill(BLUE)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("wOmP wOmP", 48, WHITE, WIDTH / 2, HEIGHT / 4 - 48)

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False


game = Game()
game.start_screen()
while game.running:
    game.reset()
    game.end_screen()

pg.quit()
