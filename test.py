#%% [markdown]
# ## Gradient Descent in Python

21414325413653regfdgfdsgew



#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

#%% [markdown]
# ### Function Y = (x + 5)**2 and Plot the function

#%%

x = np.arange(-50, 50, 0.1)
y = (x+5)**2
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, color='lightblue', marker='.', markersize=1, alpha=0.6)
ax.plot(10,10, 'rx')

#%% [markdown]
# ### Gradient Descent Algorithm

#%%
# start_point
cur_x = random.randint(-40,40)
learning_rate = 0.01
iters = 0
precision = 0.001
max_iters = 10000
previous_step_size = 1
derivative = lambda x: 2*(x+5)


#%%
while previous_step_size > precision and iters < max_iters:
    prev_x = cur_x
    cur_x = prev_x - learning_rate * derivative(cur_x)
    previous_step_size = abs(cur_x - prev_x)
    iters += 1
    time.sleep(0)
#     print("Iteration", iters, "\nX value is", cur_x)
print("The local minimum occurs at", cur_x)





