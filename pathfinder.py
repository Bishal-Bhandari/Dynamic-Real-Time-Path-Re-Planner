import networkx as nx
import heapq
import numpy as np

class Pathfinder:
    def __init__(self, G):
        self.G = G
        self.blocked_edges = set()

    def block_edge(self, u, v):
        self.blocked_edges.add((u, v))
        self.blocked_edges.add((v, u))

    def find_path(self, start, goal):
        G = self.G

        frontier = [(0, start)]
        came_from = {start: None}
        g = {start: 0}

        while frontier:
            _, current = heapq.heappop(frontier)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in G.neighbors(current):
                # skip obstacles
                if (current, neighbor) in self.blocked_edges:
                    continue

                cost = G[current][neighbor][0]["length"]
                new_cost = g[current] + cost

                if neighbor not in g or new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

        return []

    def heuristic(self, n1, n2):
        x1, y1 = self.G.nodes[n1]["x"], self.G.nodes[n1]["y"]
        x2, y2 = self.G.nodes[n2]["x"], self.G.nodes[n2]["y"]
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, came_from, node):
        path = [node]
        while came_from[node] is not None:
            node = came_from[node]
            path.append(node)
        return path[::-1]
