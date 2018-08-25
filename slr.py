# Calculates SLR and returns the equation parameters

import numpy as np
import matplotlib.pyplot as plt
import tkinter

def getslr(X, Y):
    num = den = 0
    meanx = np.mean(X)
    meany = np.mean(Y)
    m = len(X)
    for i in range(m):
        num = (X[i] - meanx) * (Y[i] - meany)
        den = (X[i] - meanx) ** 2
    B1 = num / den
    B0 = meany - (B1 * meanx)
    return(B0, B1)

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "b", marker = "o", s = 30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color = "g")

    # putting labels
    plt.xlabel('Volatile Acidity')
    plt.ylabel('Wine Quality')

    # function to show plot
    plt.show()
