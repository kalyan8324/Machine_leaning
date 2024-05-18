# 1. Data preprocessing Handle missing data
#  1. Data preprocessing Handle outliers
# 2. Linear Regression Using Multple varibles 
#  salary = m1 * test_score(out of 10) + m2 * experience + m3 * interview_score(out of 10) + b
# 3. Linear Regression Using One varible
#  m1, m2, m3 = coefficients
#  b = intercept
# test_score(out of 10) , experience ,  interview_score(out of 10)  =  independent varibles 
# salary = dependent varible

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import math
from word2number import w2n

df = pd.read_csv('/home/maren/Downloads/hiring.csv')
median = math.floor(df['test_score(out of 10)'].mean())
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(median)
df['experience'] = df['experience'].fillna('0')
df['experience'] = df['experience'].astype(str)
df['experience'] = df['experience'].apply(w2n.word_to_num)
model = linear_model.LinearRegression()
model.fit(df[['test_score(out of 10)','experience','interview_score(out of 10)']],df['salary($)'])
print("predication => ",model.predict([[12,10,10]]))
print(df)


