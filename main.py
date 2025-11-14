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


# Main Loop
def main():
    config = load_config()
    screen, clock = init_pygame(config)
    pathfinder = Pathfinder(config)


# Run App
if __name__ == "__main__":
    main()
