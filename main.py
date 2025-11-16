import pygame
import yaml
from pathfinder import Pathfinder
import sys

# Load YAML Configuration
def load_config(path="config.yaml"):
    try:
        with open(path, "r") as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print(" config.yaml not found. Please make sure it exists.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f" YAML parsing error: {e}")
        sys.exit(1)

# Initialize Pygame
def init_pygame(config):
    pygame.init()
    grid = config["grid"]
    width, height, cell_size = grid["width"], grid["height"], grid["cell_size"]

    screen = pygame.display.set_mode((width * cell_size, height * cell_size))
    pygame.display.set_caption("Dynamic Path Re-Planner")
    clock = pygame.time.Clock()
    return screen, clock

# Draw Grid / Objects
def draw_grid(screen, config, obstacles, start, goal, path):
    colors = config["colors"]
    grid = config["grid"]
    cell_size = grid["cell_size"]

    screen.fill(colors["background"])
    # Draw obstacles
    for (x, y) in obstacles:
        pygame.draw.rect(screen, colors["obstacle"],
                         (x * cell_size, y * cell_size, cell_size, cell_size))

    # Draw path
    if path:
        for (x, y) in path:
            pygame.draw.rect(screen, colors["path"],
                             (x * cell_size, y * cell_size, cell_size, cell_size))

# Main Loop
def main():
    config = load_config()
    screen, clock = init_pygame(config)
    pathfinder = Pathfinder(config)
    grid = config["grid"]
    start = (1, 1)
    goal = (grid["width"] - 2, grid["height"] - 2)
    obstacles = set()
    path = pathfinder.find_path(start, goal, obstacles)

    running = True
    while running:
        clock.tick(config["visualization"]["refresh_rate"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Draw obstacles dynamically
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                grid_x, grid_y = x // grid["cell_size"], y // grid["cell_size"]
                obstacles.add((grid_x, grid_y))

            # Clear obstacles
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.key.key_code(config["interaction"]["clear_key"]):
                    obstacles.clear()

        # Recalculate path dynamically
        path = pathfinder.find_path(start, goal, obstacles)
        draw_grid(screen, config, obstacles, start, goal, path)

    pygame.quit()

# Run App
if __name__ == "__main__":
    main()
