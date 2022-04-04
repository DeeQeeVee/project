fi = open("MINK.inp","r")
fo = open("MINK.out","w")

# tạo list chứa các phần tử , số đếm và độ dài list

A = fi.readline().split()
B = int(fi.readline())
dem = len(A)

# chuyển kiểu dữ liệu của list sang int

for j in range(dem):
    A[j] = int(A[j])

# kiểm tra điều kiện có gặp số trừng lặp hay ko

sai = 0
for i in range(dem):
    if A.count(A[i]) == 1:
        pass
    else :
        sai +=1
if sai == 0:
    if 1<B<dem:    # kiểm tra điều kiện cuối ròi sort mảng A , copy mảng A đầu vô C , tìm số bé thứ B trong A và tìm vị trí của nó trong C
        C = list(A)
        A.sort()
        print(A[B-1])
        print(C.index(int(A[B-1]))+1)