file_input = open("CNTNUM.inp", "r")
file_output = open("CNTNUM.out", "w")

a, b, c, d = map(int,file_input.read().split())
m, n = c, d
to = b - a + 1

if m == n:
        F = [n]

else:
        bcnn = c*d

        while c != d:

                if c > d: 
                        c -= d
                else:
                        d -= c
        bcnn = bcnn // c

        if bcnn in [m,n]:
                F= [min([m,n])]

        else:
                F = [m,n,bcnn]

for i in F:
        if a % i == 0:
                t = b//i - a//i + 1

        else:
                t = b//i - a//i

        if len(F)>1 and i == bcnn:
                t = -t

        to -= t
print(to, file = file_output)
