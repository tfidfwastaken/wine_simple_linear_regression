# Calculates RMSE

import math
import numpy as np

def eval_rmse(Y, Yi, n):
    error = math.sqrt((1/n) * np.sum((Y - Yi) ** 2))
    return error
