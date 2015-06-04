#!/usr/bin/env python

import pygame

# Initialize the screen
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((480, 320))

surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((0, 0, 0))

# Draw some text
font = pygame.font.SysFont("Arial", 24)
text_surface = font.render("The Holodeck", 1, (0, 255, 0))
text_pos = text_surface.get_rect()
surface.blit(text_surface, text_pos)

# Render the surface
screen.blit(surface, (0, 0))
pygame.display.flip()

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
