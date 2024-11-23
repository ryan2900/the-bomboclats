import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racecar Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Car dimensions
CAR_WIDTH, CAR_HEIGHT = 50, 100

# Player 1 car
player1 = pygame.Rect(WIDTH // 4 - CAR_WIDTH // 2, HEIGHT - CAR_HEIGHT - 10, CAR_WIDTH, CAR_HEIGHT)

# Player 2 car
player2 = pygame.Rect(3 * WIDTH // 4 - CAR_WIDTH // 2, HEIGHT - CAR_HEIGHT - 10, CAR_WIDTH, CAR_HEIGHT)

# Speeds
car_speed = 5

# Finish line
finish_line = pygame.Rect(0, 50, WIDTH, 10)

# Game loop
def game_loop():
    player1_speed = [0, 0]
    player2_speed = [0, 0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player 1 controls (Arrow keys)
        keys = pygame.key.get_pressed()
        player1_speed = [0, 0]
        player2_speed = [0, 0]

        if keys[pygame.K_LEFT]:
            player1_speed[0] = -car_speed
        if keys[pygame.K_RIGHT]:
            player1_speed[0] = car_speed
        if keys[pygame.K_UP]:
            player1_speed[1] = -car_speed
        if keys[pygame.K_DOWN]:
            player1_speed[1] = car_speed

        # Player 2 controls (WASD)
        if keys[pygame.K_a]:
            player2_speed[0] = -car_speed
        if keys[pygame.K_d]:
            player2_speed[0] = car_speed
        if keys[pygame.K_w]:
            player2_speed[1] = -car_speed
        if keys[pygame.K_s]:
            player2_speed[1] = car_speed

        # Move players
        player1.move_ip(*player1_speed)
        player2.move_ip(*player2_speed)

        # Boundaries
        player1.clamp_ip(screen.get_rect())
        player2.clamp_ip(screen.get_rect())

        # Check for finish line crossing
        if player1.colliderect(finish_line):
            winner_text("Player 1 Wins!")
            return
        if player2.colliderect(finish_line):
            winner_text("Player 2 Wins!")
            return

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, finish_line)
        pygame.draw.rect(screen, RED, player1)
        pygame.draw.rect(screen, BLUE, player2)

        pygame.display.flip()
        clock.tick(FPS)


def winner_text(winner):
    font = pygame.font.Font(None, 74)
    text = font.render(winner, True, BLACK)
    screen.fill(WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)


if __name__ == "__main__":
    game_loop()
