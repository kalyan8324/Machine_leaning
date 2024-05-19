import matplotlib.pyplot as plt

x= [1,2,3,4,5,6]
y = [50,12,48,52,66,44]
plt.plot(x,y,color='red',marker='+',alpha=0.5)
plt.plot_date(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("my first graph")
plt.show()

