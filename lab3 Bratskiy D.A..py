import math

# x1 = int(0)
# xn = int(5)
# dx = 0.5
# a = 0.5
# b = 0.7

# per = int(xn - x1)

# y = int(math.sin(a * x1) + 3 * (math.cos(b * (x1 ** 2) + 1))**2)
#
# for x in range(x1, xn):
#     if x1 <= xn:
#         print(y)
#         x1 += dx


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