
import gmpy2
n= 92323032016735545564669921985320000244114757437882665811969290814754961456436884648109047049537997174091217591128908955035057851804628537110209625589730144047166711556723392583795647752685190464911004762110190170169614931319612260910961852393814783406980753711632089394987875359845869446171420929689358873123

e= 65537


import gmpy2
#General Number Field Sieve

def factorize(n):
    p=gmpy2.mpz(n)
    factor_p=gmpy2.isqrt(p) + 1
    factor_q_squared = factor_p * factor_p - p
    while not gmpy2.is_square(factor_q_squared):
        factor_p += 1
        factor_q_squared = factor_p * factor_p - p
    factor_q=gmpy2.isqrt(factor_q_squared)
    return factor_p-factor_q,factor_p+factor_q

p,q=factorize(n)
print(p,q)

