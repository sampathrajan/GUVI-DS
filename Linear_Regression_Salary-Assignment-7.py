import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_fwf("salary.txt", header=None, 
                 names=["Sex", "Rank", "Year", "Degree", "YSdeg", "Salary"])

feature_with_sex= ['Sex', 'Rank', 'Year', 'Degree', 'YSdeg']
x = df[feature_with_sex]
y = df.Salary
model=linear_model.LinearRegression()
model.fit(x,y)
all_five_R_sqaure = model.score(x, y)
print("All Five R-Square Score: ", all_five_R_sqaure)
print("All Five Intercept: ", model.intercept_)
print("All Five Coefficients: ", model.coef_)

feature_without_sex= ['Rank', 'Year', 'Degree', 'YSdeg']
x = df[feature_without_sex]
y = df.Salary
model=linear_model.LinearRegression()
model.fit(x,y)
r_sqaure = model.score(x, y)
print("R-Square Score witout 'Sex': ", r_sqaure)
print("Intercept Without 'Sex': ", model.intercept_)
print("Coefficients Without 'Sex': ", model.coef_)

print("R-Square value is remains Same With or without the 'Sex' Column, So 'Sex' Column is inappropriate for salary.")