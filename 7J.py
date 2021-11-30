import numpy as np

def calculate(start_points: np.ndarray, end_points: np.ndarray, point: np.ndarray) -> np.ndarray:
    return np.around(abs(np.cross(end_points - start_points, point - start_points)) / np.linalg.norm(end_points - start_points, axis=1), decimals=4)
