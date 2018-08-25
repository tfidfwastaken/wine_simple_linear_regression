### Plotting a simple linear regression for the Portuguese red Vinho Verde wine

Sources for the satisfaction of the anti-plagiarism gods:
This is where I used code for the matplotlib part: https://www.geeksforgeeks.org/linear-regression-python-implementation/

In this project I find the simple linear regression equation for the dataset and predict the quality of wine for a certain value of volatile acidity.
I also plot the regression line.

**Validity of the regression line**
The RMSE value turned out to be 0.94 for the output having a range of 0-10, which makes my regression line fairly accurate.

**Inferences**
The regression line has a maximum value of 6.51, which makes all Vinho Verde wine expected to be poor or mediocre as per my arbitrary criteria for wine quality (less than 8/10).
Or maybe you shouldn't take this data seriously because there is a lot more to wine than just the volatile acidity.
(Stay tuned for multiple regression)
