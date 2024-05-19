#  The decision tree algorithm is type based modeling under supervised machine leaning
#  Dession tree are primirily used solve classification problem s 
#  CART (Classification and regression Trees) (GINI index which is determine which features to use and the order of the features in the process
#  ID3 (Iterative Dichotomiser 3) => this type of tree uses a value Called information tree or Entropy to determine which feature to use 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
import math


df  = pd.read_csv('/home/maren/Downloads/titanic.csv')
new_data = df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns')
dummies = pd.get_dummies(new_data['Sex'])
dummies = dummies.astype(int)
new_data = pd.concat([new_data,dummies],axis='columns')
new_data = new_data.drop(['Sex'],axis='columns')
new_data['Age'] = new_data['Age'].fillna(0)
new_data['Fare'] = new_data['Fare'].fillna(0)
new_data['Age'] = new_data['Age'].apply(math.floor)
new_data['Fare'] = new_data['Fare'].apply(math.floor)
model = tree.DecisionTreeClassifier()
model.fit(new_data[['Pclass','Age','Fare','female','male']],new_data['Survived'])
print(model.score(new_data[['Pclass','Age','Fare','female','male']],new_data['Survived']))
print(new_data.head())
print(model.predict([[1,28,71,1,0]]))
