import sys
import pygame

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game state
robot_x, robot_y = 5, 5
direction = "NONE"  # Can be "UP", "DOWN", "LEFT", "RIGHT"

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Robot Simulator")
clock = pygame.time.Clock()


def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.rect(screen, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)

def draw_robot(x, y):
    pygame.draw.rect(screen, RED, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


def main():
    global robot_x, robot_y, direction
    trail = [] 
    while True:
        screen.fill(BLACK)
        draw_grid()

        for pos in trail:
             pygame.draw.rect(screen, (0, 255, 255), (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        draw_robot(robot_x, robot_y)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"

        # Move robot in the current direction
        if direction == "LEFT" and robot_x > 0:
            robot_x -= 1
        elif direction == "RIGHT" and robot_x < SCREEN_WIDTH // GRID_SIZE - 1:
            robot_x += 1
        elif direction == "UP" and robot_y > 0:
            robot_y -= 1
        elif direction == "DOWN" and robot_y < SCREEN_HEIGHT // GRID_SIZE - 1:
            robot_y += 1


        trail.append((robot_x, robot_y))
        if len(trail) > 18:
            trail.pop(0)


        pygame.display.update()
        clock.tick(5)  # Adjust movement speed 


if __name__ == "__main__":
    main()
