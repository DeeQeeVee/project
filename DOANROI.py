"""
- Đọc dữ liệu từ tệp DOANROI.inp: số n, và list a, list b.
- Tạo list id lưu chỉ số ban đầu của các đoạn thẳng.
- Sắp xếp các đoạn tăng theo đầu phải b, nếu b bằng nhau thì sắp theo a tăng dần.
- Khởi tạo: lấy đoạn 1, đặt r = b1 là đầu phải của đoạn này. k = 0, v = []
- Với mỗi đoạn i: i=2..n tiếp theo ta xét:
- Nếu đầu trái của đoạn i, ai > r thì lấy đoạn i đưa vào kết quả (k=k+1,v=v+id[i]) và chỉnh r là đầu phải của đoạn i. r = bi.
- Ghi k và v ra tệp DOANROI.out
"""

#***Code***

# - Đọc dữ liệu từ tệp DOANROI.INP: số n, và list a, list b.
# - Tạo list id lưu chỉ số ban đầu của các đoạn thẳng.

file_input = open("DOANROI.inp", "r")
file_output = open("DOANROI.out", "w")
li = file_input.readline()
n = int(li)
a = []
b = []
id = []
s = 0
for li in file_input:
    ls = li.split()
    a.append(int(ls[0]))
    b.append(int(ls[1]))
    id.append(s+1)
    s += 1

# - Sắp xếp các đoạn tăng theo đầu phải b, nếu b bằng nhau thì sắp theo a tăng dần.

def qs (d,c):
    i = d
    j = c
    bm = b[(i+j)//2]
    am = a[(i+j)//2]
    while i <= j:
        while (b[i] < bm) or ((b[i] == bm) and (a[i] < am)):
            i = i + 1
        while (b[j] > bm) or ((b[i] == bm) and (a[j] > am)):
            j = j - 1
        if i <= j:
            a[i],a[j] = a[j],a[i]
            b[i],b[j] = b[j],b[i]
            id[i],id[j] = id[j], id[i]
            i = i + 1
            j = j - 1
    if d < j:
        qs(d,j)
    if i < c:
        qs(i,c)

qs(0,n-1)

# - Khởi tạo: lấy đoạn 1, đặt r = b1 là đầu phải của đoạn này. k = 1, v = [id[0]]

r = b[0]
k = 1
v = [id[0]]

# - Với mỗi đoạn i: i=1..n-1 tiếp theo ta xét:
# - Nếu đầu trái của đoạn i, ai > r thì lấy đoạn i đưa vào kết quả (k=k+1,v=v+id[i]) và chỉnh r là đầu phải của đoạn i. r = bi.

for i in range(1,n):
    if a[i] >= r:
        k += 1
        v.append(id[i])
        r = b[i]

# - Ghi k và v ra tệp DOANROI.out

print(k, file = file_output)
for i in v:
    print(i,file = file_output)

file_input.close()
file_output.close()
