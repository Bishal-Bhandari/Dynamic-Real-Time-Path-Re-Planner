import osmnx as ox
from osmnx import distance

class GraphLoader:
    def __init__(self, config):
        self.config = config

    def load_graph(self):
        cfg = self.config["map"]
        print("getting map from OSM…")

        G = ox.graph_from_place(
            cfg["place_name"],
            network_type=cfg["network_type"],
            simplify=cfg["simplify"]
        )

        # Add edge lengths (OSMnx 2.x compatible)
        distance.add_edge_lengths(G)

        self.G = G
        print("✅ Map loaded with", len(self.G.nodes), "nodes")
        return self.G

    def get_graph_bounds(self):
        xs = [data["x"] for _, data in self.G.nodes(data=True)]
        ys = [data["y"] for _, data in self.G.nodes(data=True)]
        return min(xs), max(xs), min(ys), max(ys)

    def project_to_screen(self, width, height):
        minx, maxx, miny, maxy = self.get_graph_bounds()

        self.scale_x = width / (maxx - minx)
        self.scale_y = height / (maxy - miny)

        self.minx = minx
        self.miny = miny

    def gps_to_screen(self, lon, lat):
        x = (lon - self.minx) * self.scale_x
        y = (lat - self.miny) * self.scale_y
        return int(x), int(y)
