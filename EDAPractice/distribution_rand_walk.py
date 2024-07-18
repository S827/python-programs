import numpy as np
import matplotlib.pyplot as plt

all_walks = []

for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step += 1
        else:
            step = step + np.random.randint(1, 7)
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk[-1])
    print(all_walks)
    print(all_walks[-1])

np_aw = np.array(all_walks)
# plt.plot(np_aw)
# plt.show()
print(np_aw)
# plt.clf()
np_aw_t = np.transpose(np_aw)
print(np_aw_t)
print(np_aw == np_aw_t)
plt.hist(np_aw_t)
plt.show()