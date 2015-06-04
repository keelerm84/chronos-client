#!/usr/bin/env python

import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((0, 32, 0))


# Draw text
font = pygame.font.SysFont('Arial', 24)
text_surface = font.render("Hello, World", 1, (0, 255, 0))
text_pos = text_surface.get_rect()
surface.blit(text_surface, text_pos)


screen.blit(surface, (0, 0))
pygame.display.flip()



while True:
    # Monitor for quit events.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            mainloop.quit()
