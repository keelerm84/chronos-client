#!/usr/bin/env python

from view_matrix import ViewMatrix
from view_schedule import ViewSchedule

import pygame
import threading
import time

WIDTH=800
HEIGHT=480

class Application:
    def __init__(self):
        self.models = []
        self.views = []

        matrix = ViewMatrix()
        self.models.append(matrix)
        self.views.append(matrix)

        self.views.append(ViewSchedule())

        self.queue_draw = True

    def run(self):
        # Initialize the screen
        pygame.init()
        pygame.mouse.set_visible(False)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        while True:
            # Monitor for quit events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Allow models to update.
            for model in self.models:
                if model.update():
                    self.queue_draw = True

            # Trigger a render if any models changed.
            if self.queue_draw:
                self.queue_draw = False
                self.render(screen)
            else:
                time.sleep(0.1)

    def render(self, screen):
        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()
        surface.fill((0, 0, 0))

        for view in self.views:
            view.render(surface)

        screen.blit(surface, (0, 0))
        pygame.display.flip()
