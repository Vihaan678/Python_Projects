import numpy as np
np.random.seed(42)
puppies=np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])
p=puppies.mean()
print("mean",p)
print("Standard Deviation",puppies.std())
print("Variance",puppies.var())
