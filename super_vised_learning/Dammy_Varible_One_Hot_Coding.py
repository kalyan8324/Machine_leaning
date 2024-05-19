import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.pyplot as plt



df  = pd.read_csv('/home/maren/Downloads/carprices.csv')
plt.scatter(df['Age(yrs)'],df['Sell Price($)'])
plt.xlabel('Age(yrs)')
plt.ylabel('Sell Price($)')
plt.title('Car Price vs Age')
plt.show()
dummies = pd.get_dummies(df['Car Model'])
dummies = dummies.astype(int)
df1 = pd.concat([df, dummies], axis=1)
df2 = df1.drop(['Car Model','Mercedez Benz C class'], axis=1)
model = linear_model.LinearRegression()
model.fit(df2[['Mileage', 'Age(yrs)','Audi A5','BMW X5']], df2['Sell Price($)'])
print(df)
predic = model.predict([[86000,7,0,1]])
print(model.score())

print(predic)

