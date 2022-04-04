file_input = open("soluong.inp", "r")
file_output = open("soluong.out", "w")
n, A, k = file_input.read().split("\n")
n, A, k = int(n), A.split() , int(k)
A = [int(i) for i in A]
d = 0
for i in range(n-1):
    for j in range(i+1,n):
        if A[i] + A[j] == k:
            d += 1
print(d,file=file_output)
file_input.close()
file_output.close()
