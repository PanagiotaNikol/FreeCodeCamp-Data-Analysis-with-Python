import numpy as np

def calculate(list):

    # Ελέγχουμε ότι η λίστα περιέχει ακριβώς 9 αριθμούς
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Μετατρέπουμε τη λίστα σε NumPy array 3x3
    matrix = np.array(list).reshape(3, 3)

    # Υπολογίζουμε mean, variance, standard deviation,
    # max, min και sum για:
    # 1. τις στήλες (axis=0)
    # 2. τις γραμμές (axis=1)
    # 3. ολόκληρο τον πίνακα
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item()
        ],

        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item()
        ],

        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item()
        ],

        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item()
        ],

        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item()
        ],

        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item()
        ]
    }

    return calculations

