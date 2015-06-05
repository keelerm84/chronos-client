#!/usr/bin/env python

import pygame
import time
import os

WIDTH = 800
HEIGHT = 480

ASSETS = os.path.dirname(os.path.realpath(__file__)) + "/assets"
HEADER_FONT = ASSETS + "/starjedi.ttf"
TIME_FONT = ASSETS + "/museo-300.otf"
MEETING_FONT = ASSETS + "/museo-700.otf"

class View:
    def __init__(self):
        # Initialize the screen
        pygame.init()
        pygame.mouse.set_visible(False)

        self.background = pygame.image.load(ASSETS + "/holodeck.png")

        self.queue_draw = True

    def run(self):
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        while True:
            # Monitor for quit events.
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    mainloop.quit()
                elif event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()
                    if pygame.K_ESC in pressed:
                        pygame.quit()

            # If nothing has changed then sleep momentarily
            if not self.queue_draw:
                time.sleep(0.01)
                continue

            self.queue_draw = False

            # Blank the background
            surface = pygame.Surface(screen.get_size())
            surface = surface.convert()
            surface.fill((0, 0, 0))

            # Render the changes
            self.render(surface)
            screen.blit(surface, (0, 0))
            pygame.display.flip()

    def render(self, surface):
        surface.fill((0, 0, 0))

        # Draw room background
        surface.blit(self.background, (0, 0))

        # Draw availability bar
        rect = pygame.Rect(0, 0, 75, HEIGHT)
        pygame.draw.rect(surface, (200, 0, 0), rect) 

        # Draw clock
        font = pygame.font.Font(TIME_FONT, 48)
        text_surface = font.render("12:34 PM", True, (255, 255, 255))
        text_surface = pygame.transform.rotate(text_surface, 90)
        text_pos = text_surface.get_rect()
        text_pos.bottom = HEIGHT - 40
        text_pos.left = 5
        surface.blit(text_surface, text_pos)

        # The name of the conference room
        font = pygame.font.Font(HEADER_FONT, 72)
        text_surface = font.render("The Holodeck", True, (255, 255, 255))
        text_pos = text_surface.get_rect()
        text_pos.top = 25
        text_pos.left = 110
        surface.blit(text_surface, text_pos)

        meetings = [
            {"time": "01:00 PM", "name": "Interview"},
            {"time": "01:30 PM", "name": "Sprint Planning"},
            {"time": "02:00 PM", "name": "Tech Team L10"},
            {"time": "03:00 PM", "name": "Dev Days Recap"},
            {"time": "04:00 PM", "name": "Design Patterns Book Club"},
        ]

        for i in range(0, 5):
            if i >= len(meetings):
                break

            # Meeting time
            font = pygame.font.Font(TIME_FONT, 28)
            text_surface = font.render(meetings[i]["time"], True, (255, 255, 255))
            text_pos = text_surface.get_rect()
            text_pos.bottom = 215 + 55 * i
            text_pos.left = 125
            surface.blit(text_surface, text_pos)

            # Meeting name
            font = pygame.font.Font(MEETING_FONT, 32)
            text_surface = font.render(meetings[i]["name"], True, (255, 255, 255))
            text_pos = text_surface.get_rect()
            text_pos.bottom = 215 + 55 * i
            text_pos.left = 275
            surface.blit(text_surface, text_pos)

if __name__ == "__main__":
    view = View()
    view.run()
