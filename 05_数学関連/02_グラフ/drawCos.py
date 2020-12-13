#%matplotlib inline
import matplotlib.pyplot as plt
import math

# データ
x = []
y = []
for i in range(0, 721):
    x.append(i)
    y.append(math.cos(math.radians(i))) 

#print(x)
#print(y)
plt.plot(x, y)
plt.grid(color='0.8')
plt.xlabel("kakudo")
plt.ylabel("cos")
plt.show()