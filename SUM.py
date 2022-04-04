fi = open("SUM.inp","r")
fo = open("SUM.out","w")

dem_1 = int(fi.readline()) #số phần tử của các đường chéo đang tính
dem_2 = dem_1
sum_1 = []

# đẩy từng dòng data vào 1 list
for i in range(dem_1):
    hang = fi.readline().split()
    sum_1.append(hang)

i = 0  #i, j là vị trí đang đứng
j = 0
max_1 = 0
max_2 = 0

tongmax = []

#tìm giá trị các hàng chéo phụ tính từ bên phải chéo chính
for n in range(dem_1-1):    
    j = n #để thay đổi theo giá trị n, từ đó tính các giá trị chéo phụ từ phải qua lần lượt
    for m in range(dem_1):
        max_1 = max_1 + int(sum_1[i][j])
        i += 1  #tăng dần để truy cập phần từ chéo phụ
        j += 1
    tongmax.append(max_1)
    dem_1 = dem_1-1
    max_1 = 0
    i = 0 #reset i

i = 0
j = 0

#code ngược lại ta có chéo phụ tính từ trái chéo chính
for n in range(dem_2-1):
    i = n #tác dụng ngược lại so với commit phía trên
    for m in range(dem_2):
        max_2 = max_2 + int(sum_1[i][j])
        i += 1
        j += 1
    tongmax.append(max_2)
    dem_2 = dem_2-1
    max_2 = 0
    j = 0

print(max(tongmax), file = fo)