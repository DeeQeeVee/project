import math

file_input = open("SPNUM.inp", "r")
file_output = open("SPNUM.out", "w")
n = int(file_input.readline())
a = [0] * 10000001

l = math.sqrt(n)
for i in range(2, int(math.sqrt(l)) + 1):
        if a[i] == 0:
                for j in range(i + i, int(l) + 1, i):
                        a[j] = 1
count = 0

for i in range(2, int(l) + 1):
        if a[i] == 0 and (i * i <= n):
                count += 1

        if a[i] == 0 and (i * i > n):
                break

print(count, file = file_output)