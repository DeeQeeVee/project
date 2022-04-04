"""Phương pháp: chỉ cần truy tìm 2 vị trí là hàng ngang rồi hàng dọc
để tìm khoảng cách ngắn nhất, dùng chung khoảng cách và giá trị lớn nhất để cập nhật lại thôi"""

#tao file
file_input = open("NZTABLE.inp", "r")
file_output = open("NZTABLE.out", "w")

n = int(file_input.readline())
A = []
B = []

def  pq(A, i, j, n):   #tìm vị trí p, q thoả mãn đề bài
    kc = n #khoảng cách
    kq = 0 #kết quả

    for a in range(n):
        if A[a][j] > 0 and abs(i-a) <= kc and A[a][j] > kq: #abs để tính khoảng cách giữa 2 vị trí
            kc = abs(i-a)
            kq = A[a][j]
            
    for b in range(n):
        if A[i][b] > 0 and abs(j-b) <= kc and A[i][b] > kq:
            kc = abs(j-b)
            kq = A[i][b]
    return kq


for line in file_input:
    A.append(line.split())


for i in range(n):
    for j in range(n):
       A[i][j]= int(A[i][j])


for i in range(n):
    b = []
    for j in range(n):
       if A[i][j] > 0:
           b.append(A[i][j])
       else:
           b.append(pq(A,i,j,n))
    B.append(b)

for i in B:
    print(*i, file=file_output)