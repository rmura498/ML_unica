# ex1 - lab 02
import numpy as np

n = [20, 30, 40]

mu = [[0, 0],
      [5, 5],
      [-5, -5]]

# function code

n = np.array(n)
mu = np.array(mu)

assert n.size == mu.shape[0]
n_classes = mu.shape[0]
n_features = mu.shape[1]
n_sample = np.sum(n)

x = np.zeros(shape=(n_sample, n_features))
y = np.zeros(shape=(n_sample,))

start_index = 0

for k in range(n_classes):
    xk = np.random.randn(n[k], n_features) + mu[k, :]
    yk = k*np.ones(shape=(n[k], ))
    x[start_index:start_index+n[k], :] = xk
    y[start_index:start_index + n[k]] = yk
    start_index += n[k]


print(x, y)