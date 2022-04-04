fi = open("doanroi.inp", "r")
fo = open("doanroi.out", "w")

n = int(fi.readline())
a = []
b = []
id = []
for i in range(n):
    x, y = fi.readline().split()
    a.append(int(x))
    b.append(int(y))
    id.append(i+1)
fi.close()

def qsortp(i, j):
    x = i
    y = j
    m = b[(x + y) // 2]
    while x <= y:
        while b[x] < m: x = x + 1
        while b[y] > m: y = y - 1
        if x <= y:
            b[x], b[y] = b[y], b[x]
            a[x], a[y] = a[y], a[x]
            id[x], id[y] = id[y], id[x]
            x = x + 1
            y = y -1
    if i < y: qsortp(i, y)
    if x < j: qsortp(x, j)


qsortp(0, n-1)
k = 1
dd = [id[0]]
r = b[0]
for i in range(1,n):
    if (r < a[i]): 
        k += 1
        r = b[i]
        dd.append(id[i])

print(k, file = fo)
for i in dd:
    print(i, file = fo)

fo.close()