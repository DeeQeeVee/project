fi = open("DAYF.inp","r")
fo = open("DAYF.out","w")

# tạo biến chứa n và k và 1 list rỗng

A = fi.read().split()
n,k = int(A[0]),int(A[1])
F = []

# đưa các phần tử theo công thức vào trong list

for i in range(n+1):
    if i<2:
        F.append(1)
    else:
        F.append((F[i-1]+F[i-2])%128)

# sắp xếp list và tìm ra phần tử vị trí k

F.sort()
print(F)
print(F[k])