import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_fwf("brain_body.txt")
x=df['Brain']
x = x.to_frame()
y=df['Body']

x=np.array(df['Brain']).reshape((-1,1))
y=df['Body']
model=linear_model.LinearRegression()
model.fit(x,y)

plt.scatter(x, y, color='green')
plt.plot(x, model.predict(x), color='lightblue', linewidth=2)
r_square=model.score(x,y)
print('r_square:', r_square)
