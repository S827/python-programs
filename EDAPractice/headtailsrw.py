import numpy as np

np.random.seed(123)

random_walk = [0]

for i in range(100):
    step = random_walk[-1]

    dice = np.random.randint(1, 7)

    if dice <= 2:
        step = max(0, step -1)
    elif dice <= 5:
        step += 1
    else:
        step += np.random.randint(1, 7)
    random_walk.append(step)

print(random_walk)

import matplotlib.pyplot as plt
plt.title('Random walk in the state building')
plt.plot(random_walk)
plt.show()