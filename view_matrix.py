#!/usr/bin/env python

import pygame
import os
import random

ASSETS = os.path.dirname(os.path.realpath(__file__)) + "/assets"
FONT = ASSETS + "/starjedi.ttf"

COL_MAX = 23
ROW_MAX = 14

class ViewMatrix:
    def __init__(self):
        self.matrix = []
        for col in range(0, COL_MAX):
            text = []
            for row in range(0, ROW_MAX):
                text.append(random.choice("RS"))

            self.matrix.append({
                "text": text,
                "start": 0,
                "length": 0,
            })

    def render(self, surface):
        width = surface.get_width()
        height = surface.get_height()

        font = pygame.font.Font(FONT, 32)
        for col in range(0, COL_MAX):
            start = self.matrix[col]["start"]
            length = self.matrix[col]["length"]

            row = start

            for i in range(0, length):
                row = (start + i) % ROW_MAX

                color = (0, 255, 0)
                if i == length - 1:
                    color = (255, 255, 255)

                text_surface = font.render(self.matrix[col]["text"][row], True, color)
                text_pos = text_surface.get_rect()
                text_pos.top = row * 35 - 15
                text_pos.left = col * 35
                surface.blit(text_surface, text_pos)

                row = (row + 1) % ROW_MAX

        background = pygame.Surface((width, height))
        background.set_alpha(200)
        background.fill((0, 0, 0))
        surface.blit(background, (0,0))

    def update(self):
        # Change some random letters
        for i in range(0, 30):
            col = random.randint(0, COL_MAX - 1)
            row = random.randint(0, ROW_MAX - 1)
            self.matrix[col]["text"][row] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # Randomly increase length
        for i in range(0, 10):
            col = random.randint(0, COL_MAX - 1)

            length = self.matrix[col]["length"]
            if length < ROW_MAX:
                self.matrix[col]["length"] = length + 1

        # Randomly increase start point
        for i in range(0, 10):
            col = random.randint(0, COL_MAX - 1)

            start = self.matrix[col]["start"]
            length = self.matrix[col]["length"]

            if length > ROW_MAX / 4:
                self.matrix[col]["start"] = (start + 1) % ROW_MAX
                self.matrix[col]["length"] = length - 1

        return True
