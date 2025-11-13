# 🧭 Dynamic Real-Time Path Re-Planner

This project demonstrates a **real-time dynamic pathfinding system** where two points on a 2D grid are connected through the **shortest possible path**, even as **new obstacles are added during runtime**.  

It visualizes how intelligent systems (like robots or autonomous vehicles) continuously re-plan routes to avoid collisions while maintaining optimal travel distance.

---

## 🚀 Features

- ✅ Real-time path recalculation when new obstacles appear  
- ✅ Interactive environment — draw rectangles or lines as obstacles  
- ✅ Shortest path visualization (using A* or D* Lite)  
- ✅ Modular design — easy to extend for ML or RL-based path learning  
- ✅ Built with Python and Pygame for easy visualization  

---

## 🧠 Concept

Two points (Start and Goal) are placed randomly on the screen.  
You can draw **obstacles** (lines or rectangles) between them.  
The algorithm dynamically finds the **most optimal path** connecting these points while avoiding obstacles.

If obstacles change, the path is **recomputed instantly** — no restart needed.

This project explores **dynamic pathfinding algorithms** such as:

| Algorithm | Description |
|------------|--------------|
| **A\*** | Classic pathfinding, recomputes entire path |
| **D\* Lite** | Incremental search, reuses past computations for real-time replanning |

---

## 🧩 Algorithm Overview

### A* (Baseline)
A heuristic search algorithm that computes the shortest path using:
