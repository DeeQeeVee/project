fi = open("twins.inp", "r")
fo = open("twins.out", "w") 
n, k = map(int,fi.readline().split())
m = int(n ** 0.5) +1
n += 1
d = 0
F = [True]*(n)
for i in range(2,m):
    if F[i]:
        for j in range(i**2, n, i):
            F[j] = False
n -= k
for i in range(2,n):
    if F[i] == F[i+k] == True:
        d += 1
print(d,file=fo)