import pygame

from settings import *


class Camera:
    def __init__(self, game):
        self.game = game
        self.size = (width, height)
        self.offset = 0

    def update(self):
        if self.game.player.rect.centerx > self.size[0] // 2 - 100:
            self.offset = (self.game.player.rect.centerx - self.size[0] // 2 + 100) / 1
            self.game.player.rect.centerx -= self.offset
            for x in self.game.blocks.sprites():
                x.update_(-self.offset)
            # self.game.startpos[0] -= round(self.offset)

        # elif self.game.player.rect.centerx < self.size[0] // 2 - 300:
        #     self.offset = (-self.game.player.rect.centerx + self.size[0] // 2 - 100) / 5
        #     self.game.player.rect.centerx += self.offset
        #     for x in self.game.blocks.sprites():
        #         x.update_(self.offset)
        #     self.game.startpos[0] += self.offset