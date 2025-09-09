import pygame
import sys
from ball import Ball
from obstacle import Obstacle

# Pygame initialisieren
pygame.init()

# Bildschirmgröße und Titel
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Marble Madness - Basis Level")

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Hauptspiel-Schleife
def main():
    # Kugel in der Mitte der Fläche platzieren
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 15)

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Bewegung der Kugel
        ball.move(keys)

        # Bildschirm füllen
        screen.fill(WHITE)

        # Spielfläche zeichnen
        pygame.draw.rect(screen, GREEN, (100, 100, 600, 400))  # Spielfläche

        # Kugel zeichnen
        ball.draw(screen)

        # Bildschirm aktualisieren
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()