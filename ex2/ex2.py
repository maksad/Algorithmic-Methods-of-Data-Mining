import random
from scipy import stats
print('----------------', random.random())

def get_x():
    x = []
    for i in range(10):
        uniform = stats.uniform()
        sample = round(stats.uniform().rvs(1)[0], 3)
        x.append(sample)
    return x

def get_max(x):
    max_num = -1
    for i in X:
        if max_num < i:
            max_num = i
    return max_num

X = get_x()
max_num = get_max(X)

print('X', X)
print('max_num', max_num)
