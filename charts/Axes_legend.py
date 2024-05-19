import matplotlib.pyplot as plt


days = [1,2,3,4,5,6]
max_t = [50,51,55,22,44,55]
min_t = [44,55,43,46,48,49]
avg_t = [22,25,26,24,25,29]

plt.xlabel("Weathers")
plt.ylabel("Tempareture")
plt.title("Tempaere diagram")
plt.plot(days,max_t, label="Max")
plt.plot(days,min_t, label="Min")
plt.plot(days,avg_t, label="Avg")
plt.legend(loc="best" ,shadow=True,fontsize=0.5)
plt.show()