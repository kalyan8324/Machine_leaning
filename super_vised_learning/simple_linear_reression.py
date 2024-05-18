import pandas as pd
from sklearn import linear_model
import matplotlib.pylab as plt

# Read the CSV file
df = pd.read_csv("/home/maren/Downloads/Python-project/datasets/Canada_per_capita_income.csv")
print(df.tail())
print(" => ",df.loc[41]['income'])
plt.plot(df[['year']],df["income"])
plt.xlabel("price")
plt.ylabel("year")
plt.title("income prediaction")
plt.show()
# Create and fit the model
reg = linear_model.LinearRegression()
reg.fit(df[['year']], df['income'])  
year_to_predict = pd.DataFrame({'year': [2020]})
predicted_income = reg.predict(year_to_predict)
print("Coefficient:", reg.coef_[0])
print("Intercept:", reg.intercept_)
print("Predicted income for 2010:", predicted_income[0])
manual_prediction = (reg.coef_[0] * 2020) + reg.intercept_
print("Manual calculation of predicted income for 2020:", manual_prediction)
