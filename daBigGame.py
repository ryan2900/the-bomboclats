import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Golf")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
BALL_RADIUS = 10
ball_pos = [100, 300]
ball_velocity = [0, 0]
friction = 0.98

# Hole properties
HOLE_RADIUS = 15
hole_pos = [700, 300]

# Game variables
clock = pygame.time.Clock()
running = True
shooting = False

# Font
font = pygame.font.Font(None, 36)

# Helper functions
def draw_ball():
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

def draw_hole():
    pygame.draw.circle(screen, BLACK, hole_pos, HOLE_RADIUS)

def draw_power_line(start_pos, end_pos):
    pygame.draw.line(screen, BLUE, start_pos, end_pos, 3)

def calculate_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def show_message(text, color, position):
    message = font.render(text, True, color)
    screen.blit(message, position)

# Game loop
while running:
    screen.fill(GREEN)
    draw_hole()
    draw_ball()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not shooting:
            start_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP and not shooting:
            end_pos = pygame.mouse.get_pos()
            dx = start_pos[0] - end_pos[0]
            dy = start_pos[1] - end_pos[1]
            ball_velocity = [dx * 0.1, dy * 0.1]
            shooting = True

    # Ball movement
    if shooting:
        ball_pos[0] += ball_velocity[0]
        ball_pos[1] += ball_velocity[1]

        # Apply friction
        ball_velocity[0] *= friction
        ball_velocity[1] *= friction

        # Stop the ball if it's slow enough
        if abs(ball_velocity[0]) < 0.1 and abs(ball_velocity[1]) < 0.1:
            ball_velocity = [0, 0]
            shooting = False

    # Check for collision with walls
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_velocity[0] = -ball_velocity[0]
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_velocity[1] = -ball_velocity[1]

    # Check if the ball is in the hole
    if calculate_distance(ball_pos, hole_pos) < HOLE_RADIUS:
        show_message("Hole in One!", WHITE, (WIDTH // 2 - 100, HEIGHT // 2))
        ball_velocity = [0, 0]
        shooting = False

    # Power line
    if not shooting and pygame.mouse.get_pressed()[0]:
        current_pos = pygame.mouse.get_pos()
        draw_power_line(start_pos, current_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
