# -*- coding: utf-8 -*-
"""diabetes_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NWAaxM5fLwEsnPAU6IMipm-FmTTindpv
"""



"""Importing the dependencies"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

Data COllection and analyis

"""Data Collection and analysis"""

#loading the dataset to pandas datframe
diabetes_dataset=pd.read_csv('/content/diabetes.csv')

#printing first five dataset
diabetes_dataset.head()

#checking number of rows and columns
diabetes_dataset.shape

#getting the statistical measures of the data
diabetes_dataset.describe()

"""label zero non diabetic, Label one daibetic

"""

diabetes_dataset['Outcome'].value_counts()

diabetes_dataset.groupby('Outcome').mean()

#separating data and lables
X=diabetes_dataset.drop(columns='Outcome', axis=1)
Y=diabetes_dataset['Outcome']

print(X)
print(Y)



"""Data satandarization"""

scaler=StandardScaler()

scaler.fit(X)

standardized_data=scaler.transform(X)

print(standardized_data)

X=standardized_data
Y=diabetes_dataset['Outcome']

print(X)
print(Y)



"""Splitting data into training testing data"""

X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2, stratify=Y,random_state=2)

print(X.shape, X_train.shape, X_test.shape)



"""Training the model"""

classifier=svm.SVC(kernel='linear')

#training the support vector machine to classifier
classifier.fit(X_train,Y_train)

"""Model Evaluation"""



"""Accuracy score"""



#accuarcy score on the training data
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('Accuracy score of the training data:',training_data_accuracy)

#accuarcy score on the test data
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print('Accuracy score of the test data:',test_data_accuracy)



"""Making a predictive system """

input_data=(4,110,92,0,0,37.6,0.191,30)
#changing the input data to a numpy array
input_data_as_numpy_array=np.asarray(input_data)
#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
#standardize the inupt data
std_data=scaler.transform(input_data_reshaped)
print(std_data)
prediction=classifier.predict(std_data)
print(prediction)
if(prediction[0]==0):
 print('The person is not diabetic')
else:
 print('The person is diabetic')

