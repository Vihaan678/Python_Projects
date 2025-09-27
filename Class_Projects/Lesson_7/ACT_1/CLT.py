import numpy as np
import matplotlib.pyplot as plt

num = [1, 10, 15, 100]
mean = []

np.random.seed(1)

for i in num:
    x = [np.mean(np.random.randint(-40, 40, i)) for _ in range(1000)]
    mean.append(x)

fig, ax = plt.subplots(2, 2, figsize=(6, 6))
k = 0

for i in range(2):
    for j in range(2):
        ax[i, j].hist(mean[k], 10, density=True)
        ax[i, j].set_title(label=str(num[k]))
        k= k+1

plt.show()