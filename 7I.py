import numpy as np

def nearest(points: np.ndarray, a: np.ndarray) -> np.ndarray:
    return points[np.argmin(np.sqrt(np.sum((points - a)**2, axis=1)))]

# print(*nearest(np.array([[3, 3], [0, 0]]), np.array([1, 1])))
# print(*nearest(np.array([[0, 0], [3, 3]]), np.array([1, 1])))