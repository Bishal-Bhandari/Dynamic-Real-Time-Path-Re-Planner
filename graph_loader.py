import osmnx as ox
import numpy as np

class GraphLoader:
    def __init__(self, config):
        self.config = config