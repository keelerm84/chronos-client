#!/usr/bin/env python

import pygame
import time
import os

ASSETS = os.path.dirname(os.path.realpath(__file__)) + "/assets"
HEADER_FONT = ASSETS + "/starjedi.ttf"
TIME_FONT = ASSETS + "/museo-300.otf"
MEETING_FONT = ASSETS + "/museo-700.otf"

class ViewSchedule:
    def render(self, surface):
        width = surface.get_width()
        height = surface.get_height()

        # Draw availability bar
        rect = pygame.Rect(0, 0, 75, height)
        pygame.draw.rect(surface, (200, 0, 0), rect) 

        # Draw clock
        font = pygame.font.Font(TIME_FONT, 48)
        text_surface = font.render("12:34 PM", True, (255, 255, 255))
        text_surface = pygame.transform.rotate(text_surface, 90)
        text_pos = text_surface.get_rect()
        text_pos.bottom = height - 40
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
