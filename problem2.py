import numpy as np
import matplotlib.pyplot as plt
# Parameters
m1 = -500
s1 = 1
m2 = 100
s2 = 1
p = 0.5
total_size = 100000
data_size = int(input('n:'))
# Data Generator
z = np.zeros((total_size, data_size))
u = np.zeros(total_size)
x = np.random.normal(m1, s1, (total_size, data_size))
y = np.random.normal(m2, s2, (total_size, data_size))
a = np.random.rand(total_size, data_size) < p
z: np.ndarray = x + a * y
# Calculate EZ and DZ
EZ = z.mean()
DZ = z.var()
# Calculate U_i with a loop
for i in range(total_size):
    z_sum = z[i].sum()
    u[i] = (z_sum - data_size * EZ) / np.sqrt(data_size * DZ)
# Show the plot
plt.hist(u, bins=5000)
plt.title(f'n={data_size}')
plt.show()
