import numpy as np
from linear_al import matrix_gen as mg

A = mg(2, 2)
B = mg(2, 2)

print(A)
print(B)
print(A*B)
print(A@B)