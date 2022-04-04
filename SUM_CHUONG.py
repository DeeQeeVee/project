file_input = open("SUM.inp", "r")
file_output = open("SUM.out", "w")
x = int(file_input.readline())
A = file_input.read().split("\n")
for i in range(0, x):
    m = A[i]
    A[i] = m.split()
for i in range(0, x):
    for j in range(0, x):
        A[i][j] = int(A[i][j])
max = 0
for i in range(0,x):
    max = max + A[i][i]
for i in range(1, x - 1):
    j = i
    t = 0
    ma = 0
    while j < x:
        ma = ma + A[t][j]
        t = t + 1
        j = j + 1
    if ma > max:
        max = ma
for i in range(1, x - 1):
    j = i
    t = x - 1
    ma = 0
    while j >= 0:
        ma = ma + A[t][j]
        t = t - 1
        j = j - 1
    if ma > max:
        max = ma
print(max, file=file_output)
file_input.close()
file_output.close()
