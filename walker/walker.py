import pygame
import random

# Set up the display
WIDTH = 640
HEIGHT = 360
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Walker:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.steps = []

    def display(self, screen):
        for step in self.steps: 
            pygame.draw.circle(screen, BLACK, step, 1)

    def step(self):
        choice = random.randint(0, 3)
        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        else:
            self.y -= 1
        
        self.steps.append((self.x, self.y))


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Walker")
clock = pygame.time.Clock()

# Create a Walker object
w = Walker()

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    w.step()

    # Draw
    screen.fill(WHITE)
    w.display(screen)
    pygame.display.flip()

    # Maintain constant FPS
    clock.tick(FPS)

# Quit the game
pygame.quit()

