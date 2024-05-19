import matplotlib.pylab as plt
import numpy as np

BloodSugarMan = [113,85,90,65,149,88,93,412,135,80,77,82,129]
BloodSugarWomen = [36,85,78,150,415,88,93,125,135,80,77,82,412]
plt.xlabel("Blood range")
plt.ylabel("Num of patients")
plt.title("Sugar level samples")
plt.hist([BloodSugarMan,BloodSugarWomen], bins=[80,120,150],rwidth=0.9,label=["man","women"])
plt.legend()
plt.show()