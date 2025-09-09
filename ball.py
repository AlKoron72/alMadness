import pygame

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = "BLUE"
        self.vel_x = 0
        self.vel_y = 0
        self.acceleration = 0.5
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
        if self.x - self.radius < 100:  # Linke Grenze
            self.x = 100 + self.radius
            self.vel_x = 0
        if self.x + self.radius > 700:  # Rechte Grenze
            self.x = 700 - self.radius
            self.vel_x = 0
        if self.y - self.radius < 100:  # Obere Grenze
            self.y = 100 + self.radius
            self.vel_y = 0
        if self.y + self.radius > 500:  # Untere Grenze
            self.y = 500 - self.radius
            self.vel_y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)