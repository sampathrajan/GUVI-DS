import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

ground_cricket_data = {"Chirps/Second": [20.0, 16.0, 19.8, 18.4, 17.1, 15.5, 14.7,
                                         15.7, 15.4, 16.3, 15.0, 17.2, 16.0, 17.0,
                                         14.4],
                       "Ground Temperature": [88.6, 71.6, 93.3, 84.3, 80.6, 75.2, 69.7,
                                              71.6, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5,
                                              76.3]}
df = pd.DataFrame(ground_cricket_data)

x=df['Ground Temperature']
x=x.to_frame()
y=df['Chirps/Second']

model=linear_model.LinearRegression()
model.fit(x,y)
plt.scatter(x, y, color='blue')
plt.plot(x, model.predict(x), color='limegreen')

intercept= model.intercept_
coefficient=model.coef_
print('intercept:',intercept )
print('coefficient:',coefficient )
print('r-squared: ', model.score(x, y))
extrapolate=model.predict(np.array(95).reshape(1,-1))
print("Extrapolate: ",extrapolate)
interploate=(18 - intercept) / coefficient
print("Interploate: ",interploate)