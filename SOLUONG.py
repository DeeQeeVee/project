file_input = open("SOLUONG.inp","r")
file_output = open("SOLUONG.out","w")

n = int(file_input.readline())
b = list(map(int,file_input.readline().split()))
c = int(file_input.read())
d = 0
F = [0] * (10 ** 6)

for i in b:
        F[i] += 1

for i in range(c):
        if F[i] > 0:
                if F[c - i] > 0:
                        if c - i == i:
                                d += int((F[i] * (F[i] - 1)) / 2)
                        else:
                                d += F[i] * F[c - i]
                                F[c - i] = 0

file_output.write(str(d))
