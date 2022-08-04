import numpy as np


def normalize(vec: np.ndarray):
    """Normalize a vector or array of vectors.

    Args:
        vec (np.ndarray): A #1x3 or #Nx3 array of vectors to be
            normalized.

    Returns:
        np.ndarray: the normalized vector
    """
    return vec / np.expand_dims(np.linalg.norm(vec), 0)
