fi = open('dayg.inp', 'r')
fo = open('dayg.out', 'w')
A, B = list(map(int, fi.readline().split())), list(map(int, fi.readline().split()))
i = 0
j = 0
C = []
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1
if i < len(A):
    C += A[i:]
elif j < len(B):
    C += B[j:]
print(*C, file=fo)