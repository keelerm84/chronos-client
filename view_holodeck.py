#!/usr/bin/env python

import pygame
import os

ASSETS = os.path.dirname(os.path.realpath(__file__)) + "/assets"

class ViewHolodeck:
    def __init__(self):
        self.background = pygame.image.load(ASSETS + "/holodeck.png")

    def render(self, surface):
        surface.blit(self.background, (0, 0))
