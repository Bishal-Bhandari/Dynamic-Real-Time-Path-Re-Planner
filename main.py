import pygame
import yaml
from pathfinder import Pathfinder
import sys

def load_config(path="config.yaml"):
    try:
        with open(path, "r") as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print("❌ config.yaml not found. Please make sure it exists.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        sys.exit(1)



# Main Loop
def main():
    config = load_config()


# Run App
if __name__ == "__main__":
    main()
