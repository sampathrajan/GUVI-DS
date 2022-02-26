# -*- coding: utf-8 -*-
"""SVM_Assignment14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eQnWHZfLQI7g7pc-QjnJVpnPTR4EdQHx
"""

#Social_Network_Ads.csv

"""**Import libraries**"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

"""**Importing the dataset**"""

data=pd.read_csv('Social_Network_Ads.csv')
data=data.drop('User ID',axis=1)
le=LabelEncoder()
data['Gender']=le.fit_transform(data['Gender'])
x=data[['Gender','Age','EstimatedSalary']]
y=data[['Purchased']]

"""**Splitting the dataset into the Training set and Test set**"""

X_Train,X_Test,y_Train,y_Test=train_test_split(x,y,test_size=0.25,random_state=1)

"""**Feature Scaling**"""

from sklearn.preprocessing import StandardScaler
sl=StandardScaler()
X_Train=sl.fit_transform(X_Train)
X_Test=sl.transform(X_Test)

"""**Fitting SVM to the Training set**"""

from sklearn.svm import SVC
model=SVC()
model.fit(X_Train,y_Train)

"""**Predicting the Test set results**"""

y_predict=model.predict(X_Test)
y_predict

"""**Making the Confusion Matrix**"""

from sklearn.metrics import confusion_matrix,accuracy_score,plot_roc_curve
print(confusion_matrix(y_Test,y_predict))
print(accuracy_score(y_Test,y_predict))

"""**Visualising the Training set results**"""

plot_roc_curve(model, X_Train, y_Train)



"""**Visualising the Test set results**"""

plot_roc_curve(model, X_Test, y_Test)
