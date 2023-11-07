#Code by Viswaksena J/35

import numpy as np
import matplotlib.pyplot as plt
import math

def create_motion_matrix(yaw, delta_t):
    motion_matrix = np.array([[np.cos(yaw) * delta_t, 0],
                              [np.sin(yaw) * delta_t, 0],
                              [0, delta_t]])
    return motion_matrix

def update_robot_state(yaw_angle, previous_state):
    control_vector = np.array([1.0, 0.0])
    state_transition_matrix = np.array([[1.0, 0, 0],
                                       [0, 1.0, 0],
                                       [0, 0, 1.0]])
    time_step = 1.5
    updated_state = state_transition_matrix @ previous_state + create_motion_matrix(np.deg2rad(yaw_angle), time_step) @ control_vector
    return list(map(math.floor, updated_state))

def find_optimal_path(grid, path, current_state):
    grid_size = len(grid)
    current_row, current_col = current_state[0], current_state[1]

    if current_row == grid_size - 1 and current_col == grid_size - 1:
        path.append((current_row, current_col))
        return True

    if 0 <= current_row < grid_size and 0 <= current_col < grid_size and grid[current_row, current_col] == 1.0:
        path.append((current_row, current_col))
        grid[current_row, current_col] = 2.0

        possible_yaw_angles = [45, 0, 90, 135, -45, 45, 180, -90, -135]

        for angle in possible_yaw_angles:
            updated_state = update_robot_state(angle, current_state)
            if find_optimal_path(grid, path, updated_state):
                return True

        path.pop()

    return False

def visualize_optimal_path(grid):
    grid_size = len(grid)
    path = []

    if not find_optimal_path(grid, path, [0, 0, 0]):
        print("No path found.")
        return

    print("Optimal path from [0, 0] to [N-1, N-1]:")
    for row, col in path:
        print(f"[{row}, {col}]")
        grid[row, col] = 3.0

    plt.imshow(grid, cmap='gray', vmin=0, vmax=3)
    plt.show()

grid_columns = 50
grid_rows = 50
obstacle_probability = 0.8

grid = (np.random.rand(grid_rows, grid_columns) < obstacle_probability).astype(int)

visualize_optimal_path(grid)
