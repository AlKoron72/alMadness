import pygame
import sys

# Pygame initialisieren
pygame.init()

# Bildschirmgröße und Titel
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Marble Madness - Isometrisches Level")

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Funktion zur Umrechnung in isometrische Koordinaten
def to_isometric(x, y, z=0):
    iso_x = x - y
    iso_y = (x + y) / 2 - z
    return iso_x, iso_y

# Kugel-Klasse
class Ball:
    """AI is creating summary for 
    """
    
    def __init__(self, x, y, z, radius):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.color = BLUE
        self.vel_x = 0
        self.vel_y = 0
        self.acceleration = 0.3
        self.friction = 0.98

    def move(self, keys):
        # Bewegung basierend auf den Pfeiltasten
        if keys[pygame.K_LEFT]:
            self.vel_x -= self.acceleration
        if keys[pygame.K_RIGHT]:
            self.vel_x += self.acceleration
        if keys[pygame.K_UP]:
            self.vel_y -= self.acceleration
        if keys[pygame.K_DOWN]:
            self.vel_y += self.acceleration

        # Reibung anwenden
        self.vel_x *= self.friction
        self.vel_y *= self.friction

        # Position aktualisieren
        self.x += self.vel_x
        self.y += self.vel_y

        # Begrenzung der Kugel auf die Spielfläche
        if self.x < 0:
            self.x = 0
            self.vel_x = 0
        if self.x > 400:
            self.x = 400
            self.vel_x = 0
        if self.y < 0:
            self.y = 0
            self.vel_y = 0
        if self.y > 400:
            self.y = 400
            self.vel_y = 0

    def draw(self, screen):
        # Kugel in isometrischen Koordinaten zeichnen
        iso_x, iso_y = to_isometric(self.x, self.y, self.z)
        pygame.draw.circle(screen, self.color, (int(iso_x) + 400, int(iso_y) + 200), self.radius)

# Hauptspiel-Schleife
def main():
    # Kugel in der Mitte der Fläche platzieren
    ball = Ball(200, 200, 0, 15)

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

        # Spielfläche zeichnen (isometrisches Raster)
        for x in range(0, 401, 50):
            for y in range(0, 401, 50):
                iso_x, iso_y = to_isometric(x, y)
                pygame.draw.polygon(
                    screen,
                    GRAY,
                    [
                        (iso_x + 400, iso_y + 200),
                        (iso_x + 450, iso_y + 225),
                        (iso_x + 400, iso_y + 250),
                        (iso_x + 350, iso_y + 225),
                    ],
                    2,
                )

        # Kugel zeichnen
        ball.draw(screen)

        # Bildschirm aktualisieren
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()