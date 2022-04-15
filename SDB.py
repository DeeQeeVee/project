import math

file_input = open("SDB.inp", "r")
file_output = open("SDB.out", "w")

l = [0] *1001
v = []

for i in range(2, int(math.sqrt((1001)))):
        if (l[i] == 0):
                for j in range(i + i, 1001, i):
                        l[j] = 1

for i in range(2, 1001):
        if (l[i] == 0):
                v.append(i)

p = 0
f = [0] * (10**6 + 1)
for i in range(0, len(v)):
        p = v[i] *v[i] * 3 * 3

        if (p > 10**6):
                break
        f[p] = 1

p = 1
count = 0

f[6561] = 1
f[81] = 0

for i in range(36, 10**6 + 1):
        if (f[i] != 0):
                count += 1

        f[i] = count

t = file_input.readline()
t = int(t)

for i in range(0, t):
        a, b = map(int, file_input.readline().split())
        if (f[a - 1] < f[a]):
                print(f[b] - f[a] + 1, file = file_output, end = "\n")
        
        else:
                print(f[b] - f[a], file = file_output, end = "\n")