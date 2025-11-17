import pygame
import yaml
from graph_loader import GraphLoader
from pathfinder import Pathfinder

def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)

def find_closest_node(G, x, y):
    return min(G.nodes, key=lambda n: (G.nodes[n]["x"] - x)**2 + (G.nodes[n]["y"] - y)**2)

def main():
    config = load_config()

    # Load graph
    loader = GraphLoader(config)
    G = loader.load_graph()

    W = config["visualization"]["window_width"]
    H = config["visualization"]["window_height"]

    loader.project_to_screen(W, H)
    pathfinder = Pathfinder(G)

    pygame.init()
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()

    # pick start and goal
    nodes = list(G.nodes)
    start = nodes[100]
    goal = nodes[1000]

    running = True
    path = pathfinder.find_path(start, goal)

    while running:
        screen.fill(config["visualization"]["background"])
        clock.tick(config["visualization"]["refresh_rate"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Left-click = add obstacle
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()

                # find closest graph node to clicked point
                closest = min(G.nodes, key=lambda n:
                    (loader.gps_to_screen(G.nodes[n]["x"], G.nodes[n]["y"])[0] - mx)**2 +
                    (loader.gps_to_screen(G.nodes[n]["x"], G.nodes[n]["y"])[1] - my)**2
                )

                # block all edges from that node
                for neighbor in G.neighbors(closest):
                    pathfinder.block_edge(closest, neighbor)

            # Clear obstacles
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pathfinder.blocked_edges.clear()

        # Recompute path
        path = pathfinder.find_path(start, goal)

        # Draw edges
        for u, v in G.edges():
            x1, y1 = loader.gps_to_screen(G.nodes[u]["x"], G.nodes[u]["y"])
            x2, y2 = loader.gps_to_screen(G.nodes[v]["x"], G.nodes[v]["y"])

            if (u, v) in pathfinder.blocked_edges:
                color = config["colors"]["obstacle_edge"]
            else:
                color = config["colors"]["edge"]

            pygame.draw.line(screen, color, (x1, y1), (x2, y2), 1)

        # Draw path
        for i in range(len(path)-1):
            u = path[i]
            v = path[i+1]
            x1, y1 = loader.gps_to_screen(G.nodes[u]["x"], G.nodes[u]["y"])
            x2, y2 = loader.gps_to_screen(G.nodes[v]["x"], G.nodes[v]["y"])
            pygame.draw.line(screen, config["colors"]["path"], (x1, y1), (x2, y2), 4)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
