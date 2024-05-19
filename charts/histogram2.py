import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170,10,250)
print("x \n" , x)
plt.hist(x,bins=30,kde=True)
plt.show()