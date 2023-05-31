import pygame 
import random
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Distribution")

bars = [0] * 40
bar_width = WIDTH // len(bars)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    # Update bars height
    index = random.randint(0, len(bars) - 1)
    bars[index] += 1
    
    # Draw bars
    for b in range(len(bars)):
        bar_height = bars[b]
        pygame.draw.rect(screen, (0, 0, 0), (b * bar_width, HEIGHT - bar_height, bar_width - 1, bar_height))

    # Update the screen
    pygame.display.flip()

pygame.quit()