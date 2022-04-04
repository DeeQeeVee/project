""" -	Đọc bảng
    -	Viết chương trình con để kiểm tra (check): nếu một dãy 9 số thoả mãn điều kiện từ 1 đến 9 thì trả về 1, ngược lại trả về 0
    -	Khởi tạo kq = 1
    -	Duyệt từng hàng và kiểm tra, nếu ktra bằng 0 thì ngưng
    -	Nếu kq của ktra bằng 1 thì duyệt từng cột, nếu kết quả ktra trả về 0 thì ngưng
    -	Nếu kq ktra trả về 1 thì duyệt từng vùng, nếu kết quả ktra trả về 0 thì ngưng.
    -	Ghi kết quả, đóng tệp
"""

file_input = open("SUDOKU.inp", "r")
file_output = open("SUDOKU.out", "w")

# -	Đọc bảng

a = []
for line in file_input:
    teemo = line.split()
    a.append(teemo)

# -	Viết chương trình con để kiểm tra (check): nếu một dãy 9 số thoả mãn điều kiện từ 1 đến 9 thì trả về 1, ngược lại trả về 0

def check(day):
    dd = [0] * 10 
    for a in day:

        if (int(a) > 9) or (int(a) < 1):
            return 0

        dd[int(a)] += 1
        
        if dd[int(a)] > 1:
            return 0
    return 1

# -	Khởi tạo kq = 1

kq = 1

# -	Duyệt từng hàng và kiểm tra, nếu ktra bằng 0 thì ngưng

for d in a:
    kq = check(d)
    if kq == 0:
        break

# -	Nếu kq của ktra bằng 1 thì duyệt từng cột, nếu kết quả ktra trả về 0 thì ngưng

if kq == 1:
    for j in range(9):
        d = []
        for i in range(9):
            d.append(a[i][j])
        kq = check(d)
        if kq == 0:
            break

# -	Nếu kq ktra trả về 1 thì duyệt từng vùng, nếu kết quả ktra trả về 0 thì ngưng.

if kq == 1:
    di = [0, 0, 1, 1, 1, 2, 2, 2]
    dj = [1, 2, 0, 1, 2, 0, 1, 2]
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            d = []
            d.append(a[i][j])
            for k in range(8):
                d.append(a[i + di[k]][j + dj[k]])
            kq = check(d)
            if kq == 0:
                break
        if kq == 0:
            break

# -	Ghi kết quả, đóng tệp

print(kq, file = file_output)
file_input.close()
file_output.close()