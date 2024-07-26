import numpy as np
import math
v2 = np.array([846835985, 9834798552])
v1 = np.array([87502093, 123094980])

while True:
    if (math.sqrt(v2.dot(v2)) < math.sqrt(v1.dot(v1))):
        v1,v2 = v2,v1
    m = math.floor(v1.dot(v2)/v1.dot(v1))

    if (m==0):
        break
    v2 = v2 - m*v1

print(np.inner(v1,v2))