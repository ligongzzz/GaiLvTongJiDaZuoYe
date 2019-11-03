import numpy as np
import matplotlib.pyplot as plt

# Input
m1 = eval(input('μ1:'))
s1 = eval(input('σ1:'))
m2 = eval(input('μ2:'))
s2 = eval(input('σ2:'))
p = eval(input('p:'))
data_size = 10000
# Generate Random Numbers
x = np.random.normal(m1, s1, data_size)
y = np.random.normal(m2, s2, data_size)
a = np.random.rand(data_size) < p
z = x + a * y
# Show
plt.hist(z, bins=50)
plt.show()
