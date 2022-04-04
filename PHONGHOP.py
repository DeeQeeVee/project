file_input = open("PHONGHOP.inp", "r")
file_output = open("PHONGHOP.out", "w")

n = int(file_input.readline())
A, B = [], []
for line in file_input:
    a, b = line.split()
    A.append(int(a))
    B.append(int(b))

def qs (d, c):
    i = d
    j = c
    bm = B[(i+j) // 2]
    am = A[(i+j) // 2]
    while i <= j:
        while (B[i] < bm) or ((B[i] == bm) and (A[i] < am)):
            i = i + 1
        while (B[j] > bm) or ((B[i] == bm) and (A[j] > am)):
            j = j - 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            B[i], B[j] = B[j], B[i]
            i = i + 1
            j = j - 1
    if d < j:
        qs(d, j)
    if i < c:
        qs(i, c)

qs(0, n - 1)

vtDau = B[0]
soPhong = 1

for i in range(1, n):
    if A[i] >= vtDau:
        vtDau = B[i]
        soPhong += 1

print(soPhong, file = file_output)

file_input.close()
file_output.close()