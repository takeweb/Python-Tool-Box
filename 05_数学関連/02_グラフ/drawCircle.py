#%matplotlib inline
import matplotlib.pyplot as plt
import math

# データ
x = []
y = []
for i in range(0, 361):
    x.append(math.cos(math.radians(i)))
    y.append(math.sin(math.radians(i))) 

#print(x)
#print(y)
plt.plot(x, y)
plt.grid(color='0.8')
plt.xlabel("cos")
plt.ylabel("sin")
plt.show()