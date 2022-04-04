file_input = open("MINK.inp", "r")
file_output = open("MINK.out", "w")

a = file_input.readline().split()
n = len(a)
b = list(a)
k = file_input.readline()
k = int(k)
kq = 0
vt = 0

for i in range(len(a)):
    a[i] = int(a[i])
a.sort()

kq = int(a[k - 1])

for i in range(0, n):
    if int(b[i]) == kq:
        vt = i + 1
        break

print(kq, vt, file = file_output)
