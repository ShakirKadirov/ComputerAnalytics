import numpy as np

def generate_x(k):
  x = np.zeros(500)
  dt = 2 * np.pi / 1000
  L = k / 100
  omega = 1000 / k
  x[0] = 0
  x[1] = (-1)**k * dt
  for i in range(2, 500):
    x[i] = x[i-1] * (2 + dt * L * (1 - x[i-2]**2)) - (i-1) * (1 + dt**2 + dt * L * (1 - x[i-2]**2)) + dt**2 * np.sin(omega * i * dt)
  return x

k = 12

x = generate_x(k)
print(x)
