file_input = open("SPNUM.inp", "r")
file_output = open("SPNUM.out", "w")
n = int(file_input.readline())

F = [True]*(n+1)
F[0] = F[1] = False
spnum = 0
m = int(n**0.5)+1
n += 1
for i in range(2, m):
        if F[i]:
                for j in range(i**2,n,i):
                        if j  == i**2:
                                spnum += 1
        F[j] = False
print(spnum, file = file_output)

