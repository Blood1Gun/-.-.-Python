# # Лаб. работа №3
# # Братский Дмитрий, 100502-УБТа-о23, Вариант 2

# С помощью цикла for
import math

x1 = 0
xn = 5
dx = 0.5
a = 0.5
b = 0.7
per = int((xn - x1) / dx)

results = []

for x in range(per):
    x = x1 + x * dx
    y = math.sin(a * x) + 3 * (math.cos(b * (x**2) + 1))**2
    results.append((x, y))

for x, y in results:
    print(f"x = {x:.2f}, y = {y:.4f}")


# С помощью цикла While
import numpy as np

x1 = 0
xn = 5
dx = 0.5
a = 0.5
b = 0.7

results = []

x = x1
while x <= xn:
    y = np.sin(a * x) + 3 * (np.cos(b * x**2 + 1))**2
    results.append((x, y))
    x += dx

for x, y in results:
    print(f"x = {x:.1f}, y = {y:.4f}")
