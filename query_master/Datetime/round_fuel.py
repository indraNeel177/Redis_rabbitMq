# import numpy as np
# f = np.array([1, 2, 3])   # everytim e
# g = np.array([4, 5, 6])
# g1 = np.array([4, 5, 7])
# g2= np.array([4, 5, 2])
# h = np.vstack((f, g, g1, g2))
# eval = []
# rows, column = h.shape
# for rows, column in range(h.shape):
#     eval.append((h[2]) )  # here 2 is satic, fetching the 3r value
# min = min(eval)
# max = max(eval)
# avg = sum (eval)/len(eval)
# print(min, max, avg)

import math
z = 0




def float_round_off_value(float_value, round_off_value):
    return math.floor(float_value * 10 ** round_off_value) / 10 ** round_off_value

print(float_round_off_value(z,2))



f = [[1,2,3,4], [1,2,3,4]]

print(f[-1][2::])