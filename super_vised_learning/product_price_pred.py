import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

readfile =  '/home/maren/Downloads/Grocery_data.csv'
df = pd.read_csv(readfile)  
df['Category'] = df['Category'].str.replace('-',' ').apply(lambda x:x.split(' ',1)[-1])
min_price = df.loc[df['Original Price (Rs.)'].idxmin()]
max_price = df.loc[df['Original Price (Rs.)'].idxmax()]
high_discount_price = df.loc[df['Discounted Price (Rs.)'].idxmax()]
high_discount = df.loc[df['Quantity'].idxmax()]
plt.figure(figsize=(20,10))
df['Category'].value_counts().plot(kind='bar')
plt.title("Number of products in each category")
plt.xlabel('Category Name')
plt.ylabel('Count')
plt.show()
df['Discount'] = df['Discount'].str.rstrip('%').astype(float)
df['Discount'] = df['Discount'].replace('0% OFF','',regex=True)
df['Discount'] = df['Discount'].replace('% OFF',' ', regex=True).astype(float)
print(df['Discount'].head())
print("count => ",df['Category'].value_counts() , '\n     total count =>   ', len(df))
# Select relevant features and target variable
x = df[['Original Price (Rs.)','Discount']] 
y = df[['Discounted Price (Rs.)']]
# split the date into  training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# train the linear regression model on the dataset
model = LinearRegression()
print("x_train",x_train,"y_train",y_train)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
# calculate the root mean squared error of the prediction1
mse = mean_squared_error(x_test,y_pred)
print("Mean Squared Eror::",mse)
new_data = pd.DataFrame({'Original Price (Rs.)':[50],'`Discount':[0.2]})
predicted_price = model.predict(new_data)
print("Predicted price",predicted_price)



