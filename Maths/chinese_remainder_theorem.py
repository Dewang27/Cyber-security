# making a chinese remanider calculator
# values
a1=2
a2=3
a3=5

n1=5
n2=11
n3=17
N=n1*n2*n3
print(N)

#finding N1,N2,N3

N11=N/n1
N22=N/n2
N33=N/n3


print(int(N11))
print(int(N22))
print(int(N33))

#finding x1,x2,x3
x1=pow(int(N11),-1,n1)
x2=pow(int(N22),-1,n2)
x3=pow(int(N33),-1,n3)

#using int() cause pow doesnt take 3 arguments if all are not integers :(
X=a1*N11*x1+a2*N22*x2+a3*N33*x3

print(X%N)