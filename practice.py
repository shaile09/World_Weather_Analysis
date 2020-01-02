# %%
# Import the random module.
import random 

# %%
random.randint(-90,90)
#random.randint(90, 90)

# %%
x = 1
latitudes = []
while x < 11:
    random_lat = random.randint(-90, 90) + random.random()
    latitudes.append(random_lat)
    x += 1

# %%
# Import the NumPy module.
import numpy as np

# %%
np.random.uniform(-90.000, 90.000)

# %%
np.random.uniform(-90.000, 90.000, size=50)

# %%
# Import timeit.
import timeit

# %%
def latitudes(size):
    latitudes = []
    x = 0
    while x < (size):
        random_lat = random.randint(-90, 90) + random.random()
        latitudes.append(random_lat)
        x += 1
    return latitudes
# Call the function with 1500. 
%timeit latitudes(1500)

# %%
