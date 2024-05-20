import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()

df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['target'] = iris.target
df['flower_names'] = df.target.apply(lambda x:iris.target_names[x])
df1 = df[df.target == 0]
df2 = df[df.target == 1]
df3 = df[df.target == 2]
# plt.xlabel("sepal length")
# plt.ylabel("sepal width")
# plt.title("sepal length sepal width ")
# plt.scatter(df1['sepal length (cm)'],df1['sepal width (cm)'],color='green',marker='+')
# plt.scatter(df2['sepal length (cm)'],df2['sepal width (cm)'],color='blue',marker='.')
# plt.scatter(df3['sepal length (cm)'],df3['sepal width (cm)'],color='red',marker='.')


plt.xlabel("petal length ")
plt.ylabel("petal width")
plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'],color='green',marker='+')
plt.scatter(df2['petal length (cm)'],df2['petal width (cm)'],color='blue',marker='.')

plt.show()
