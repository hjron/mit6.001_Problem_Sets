import numpy as np

x = input('Enter number x: ')
y = input('Enter number y: ')

safex = int(x)
safey = int(y)

print('x**y = ', safex**safey)
print("log(x) = %.0f" % np.log2(safex))
