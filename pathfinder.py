import heapq
import numpy as np

class Pathfinder:
    def __init__(self, config):
        self.config = config

    def find_path(self, start, goal, obstacles):
        # Simple A* (replace later with D* Lite for dynamic replanning)
        width = self.config["grid"]["width"]
        height = self.config["grid"]["height"]

        open_list = []
        heapq.heappush(open_list, (0, start))
        came_from = {}
        g_score = {start: 0}