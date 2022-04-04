fi = open("bacthang.inp", "r")
fo = open("bacthang.out", "w")
n = int(fi.readline())
if n <=1:
    print(0,file=fo)
else:
    F = [0]*n
    F[0] = F[1] = 1
    for i in range(2,n):
        F[i] = F[i-1] + F[i-2]
    print(F[n-1],file = fo)