p=29
ints=[14,6,11]

def quad_residue(p,ints):
    for i in range(1,p):
        if pow(i,2,p) in ints:
            print(i) 
        
quad_residue(p,ints)
        
# 6 is quadratic residue from ints

