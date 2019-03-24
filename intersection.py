import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(0, 1000)
x = np.arange(-100, 900)
f = np.arange(0, 1000)
#g = np.sin(np.arange(0, 10, 0.01) * 2) * 1000
#g = plt.axhline(10, color='r')

# Horizontal line
value = 40
#g = np.array([value for i in range(len(x))])
g = np.array([value for i in x])

for i in x:
    print(i)
#print(range(len(x)))

plt.plot(x, f, '-')
plt.plot(x, g, '-')

idx = np.argwhere(np.diff(np.sign(f - g)) != 0).reshape(-1) + 0
plt.plot(x[idx], f[idx], 'ro')

print("X values:", x[idx])
print("Y values:", f[idx])
plt.show()