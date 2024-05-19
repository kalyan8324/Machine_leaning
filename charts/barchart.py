import numpy as np
import matplotlib.pyplot as plt

Women  = [115,251,252,200,620,780]
Men = [140,250,135,523,523,256]

x_axis = np.arange(len(Women))
plt.bar(x_axis +0.25,Women , color = 'b',  width=0.25 , edgecolor = 'black')
plt.bar(x_axis,Men, color = 'g', width=0.25,edgecolor='black')
plt.xticks(x_axis+ 0.25/2, ['2018,2019,2020','2021','2022','2023'])
plt.xlabel("Year")
plt.ylabel("Number of people")
plt.title("Women and Men")
plt.legend()
plt.show()