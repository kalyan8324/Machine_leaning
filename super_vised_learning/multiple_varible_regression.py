#  1. Data preprocessing Handle missing data
#  2. Linear Regression Using Multple varibles 
#  price = m1 * area + m2 * bedrooms + m3 * age +b
#  price = dependent varibles
#  area, bedrooms,age  = independent varibles
#  m1, m2, m3 = coefficients
#  b = intercept
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import math

df = pd.read_csv('/home/maren/Downloads/Python-project/datasets/homeprices.csv')
median = math.floor(df.bedrooms.mean())
df.fillna(median,inplace=True)
plt.plot(df)
plt.show()
model = linear_model.LinearRegression()
model.fit(df[['area','bedrooms','age']],df.price)
print("predicated values => ",model.predict([[3000,4,10]]))
# from sklearn.externals import joblib
# joblib.dump(model,'modelJobel')

print(df)