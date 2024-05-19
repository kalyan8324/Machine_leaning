import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# import seaborn as sns


# Generate some sample data 
np.random.seed(0)
# Genarate 100 random numbers between 0 and 2
X = 2*np.random.rand(100,1) 
print("x =>",np.random.rand(100,1))
# Add some noise to linear relationsip
y = 4+3 * X+np.random.randn(100,1)
print("y =>",np.random.randn(100,1))
# Split the data into traning and testing sets
print()
X_train,X_test, y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
# train the linear regression model
model = LinearRegression()
model.fit(X_train,y_train)
#  make prediction on the test data 
y_pred = model.predict(X_test)
#  Calculate Mean Squared Error
mse = mean_squared_error(y_test,y_pred)
print("Mean Squared Error: ", mse)

#  plot the data and linear regression line 
plt.scatter(X_test,y_test,color= 'blue')
plt.plot(X_test,y_pred,color = 'red')
# sns.lineplot(X_test,y_test)
plt.title('Linear Regression')
plt.xlabel('X independed varibles')
plt.ylabel('y depended varibles')
plt.show()
