import numpy as np

l1= [4,1,3,-1]
l2 = [2,1,-3,4]
l3 = [1,0,-2,7]
l4 = [6, 2, 9, -5]

v1= np.array(l1)
print(v1)
'''
v2= np.array(l2)
v3= np.array(l3)
v4= np.array(l4)

u1=v1
u2=v2 - (np.dot(v2,u1)/np.dot(u1,u1))*u1
u3=v3 - (np.dot(v3,u1)/np.dot(u1,u1))*u1 - (np.dot(v3,u2)/np.dot(u2,u2))*u2
u4=v4 - (np.dot(v4,u1)/np.dot(u1,u1))*u1 - (np.dot(v4,u2)/np.dot(u2,u2))*u2 - (np.dot(v4,u3)/np.dot(u3,u3))*u3

print(u4)'''