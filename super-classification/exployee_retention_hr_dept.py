
#  logistic regression: based on the probability and is used to predict the categorial dependent varible and independent varibles
#  Logistic regression type: 1. Binomial 2. Multinomial 3. ordinal 
#  Binomial: 1. Binary 2. Multinomial
#  Assumtion of logistic regression:
#  1. out put data is yes or no 
#  2. Linearity 
#  3. Littil out leair
#  4. Independance value 

#  steps:
#  1. import the libraries
#  2. import the dataset
#  3. data preprocessing
#  4. split the dataset into the training set and test set
#  5. create the dependent and independent variables
#  6. fit logistic regression model with the training set
#  7. predict the test set result
#  8. make the confusion matrix => accuracy of a classification model
#  9. calculate the accuracy score

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('/home/maren/Downloads/HR_comma_sep.csv')
print(df.head())
left = df[df['left']==1]
retained = df[df['left']==0]
# group_by = df.groupby(df.left).mean()
# print(group_by)
cros_tab = pd.crosstab(df['salary'],df['left'])
cros_tab.plot(kind='bar')
dept_cross = pd.crosstab(df.Department,df.left)
dept_cross.plot(kind='bar')

subdep = df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
subdep1 =subdep.head()
dummi = pd.get_dummies(subdep.salary,prefix="salary")
dummi = dummi.astype(int)
dummi_with_data = pd.concat([subdep,dummi],axis='columns')
dummi_with_data = dummi_with_data.drop('salary',axis='columns')

X = dummi_with_data
y = df.left

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3)
print(X_train.shape)
model = LinearRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))
print(model.score(X_test,y_test))


plt.title('Salary vs Employee Retention')
plt.xlabel('Salary Level')
plt.ylabel('Number of Employees')
plt.show()
