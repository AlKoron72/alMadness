import pygame
import sys

# Pygame initialisieren
pygame.init()

# Bildschirmgröße und Titel
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Marble Madness Clone")

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Hauptspiel-Schleife
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Bildschirm füllen
        screen.fill(WHITE)

        # Update und Render-Logik hier

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()