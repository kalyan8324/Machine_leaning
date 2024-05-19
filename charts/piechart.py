import matplotlib.pyplot as plt
import numpy as np

expenses = [5000,6000,6000,1000]
exp_label = ["Home","Hotel_fee","Slice","Other exp"]
plt.pie(expenses , labels=exp_label, autopct='%0.0f%%',)
plt.title("Expenses")
plt.axis("equal")
plt.legend()
plt.savefig("piechart.pdf")
plt.show()
