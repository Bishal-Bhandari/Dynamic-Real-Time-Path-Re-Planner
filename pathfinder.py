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

        while open_list:
            _, current = heapq.heappop(open_list)
            if current == goal:
                return self.reconstruct_path(came_from, current)

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < width and 0 <= neighbor[1] < height and neighbor not in obstacles:
                    tentative_g = g_score[current] + 1
                    if tentative_g < g_score.get(neighbor, np.inf):
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + abs(neighbor[0]-goal[0]) + abs(neighbor[1]-goal[1])
                        heapq.heappush(open_list, (f_score, neighbor))
                        came_from[neighbor] = current

        return []