import matplotlib.pyplot as plt
import numpy as np

company = ['GOOGLE','AMAZON','MSFT','FB','INSTA','OPEN_AI']
revenue = [160,135,120,130,150,200]
profit = [40,10,20,100,80,250]
# plt.xlabel("Companys")
# plt.ylabel("Revenues")
# plt.title("Company data")
# plt.bar(company,profit , color="red")
# plt.bar(company,revenue,color='green',label="revenue")
# plt.legend()
# plt.show()

x_axis = np.arange(len(company))
plt.bar(x_axis - 0.2 , revenue,0.4 , label = "Revenue")
plt.bar(x_axis + 0.2 , profit , 0.4 , label = "Profit")
plt.xticks(x_axis,company)
plt.xlabel("Companys")
plt.ylabel("Revenues")
plt.title("Company profit loss detaiils")
plt.legend()
plt.show()

#  i want to see side by side bar chart