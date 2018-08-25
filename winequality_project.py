"""
Simple linear regression for the red variant of the Vinho Verde wine
Parameters are quality vs volatile acidity
"""
import numpy as np
import pandas as pd # Parses CSVs
from slr import getslr, plot_regression_line
from rmse import eval_rmse

wine_data_training = pd.read_csv('winequality-red-training.csv', sep=';')
print(wine_data_training.head())
wine_data_testing = pd.read_csv('winequality-red-testing.csv', sep=';')

X = wine_data_training['volatile acidity']
Y = wine_data_training['quality']

Ytest = wine_data_testing['quality']

print("Simple Linear Regression:")
b = getslr(X, Y)
print("Equation for best fit line: ", "y = ", b[0], " + " , b[1], "x", sep = '')
rmse = eval_rmse(Y, Ytest, len(Ytest))
print("RMSE:", rmse)

userx = input("Time to predict the quality of your choicest wine! \nEnter its volatile acidity: ")
userx = float(userx)
usery = b[0] + (b[1] * userx)
print(usery)

# The regression line is such that the wine is always mediocre.
# I could make the ratings more lax, but it would betray the standards for wine snobbery
if usery > 8:
    print("Bom Proveito! You sir are a proper snob!")
elif usery > 5:
    print("You like your wine mediocre I see.")
else:
    print("Nossa! Throw away that filthy wine!")

print("Plotting the regression line...")
plot_regression_line(X, Y, b)
