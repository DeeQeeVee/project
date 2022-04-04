file_input = open("TIENMAX.inp", "r")
file_output = open("TIENMAX.out", "w")

n = int(file_input.readline())
A, B, C = [], [], []
for line in file_input:
    a, b,c = line.split()
    A.append(int(a))
    B.append(int(b))
    C.append(int(c))

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
            C[i], C[j] = C[j], C[i]
            i = i + 1
            j = j - 1
    if d < j:
        qs(d, j)
    if i < c:
        qs(i, c)

qs(0, n - 1)

for i in range(n):
    for j in range(i):
        if B[j] <= A[i]:
            C[i] = C[j] + C[i]

print(max(C), file = file_output)

file_input.close()
file_output.close()
