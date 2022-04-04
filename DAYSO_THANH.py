fi = open("DAYSO.inp","r")
fo = open("DAYSO.out","w")

n = int(fi.readline())
a = fi.read().split()
b = []

def test(i,k): 
    l = 0
    if i<=n-2:
        for j in range(k+1,n):
            b.append((int(a[i])+int(a[k])+int(a[j]))/3)
            l = j
        if l == n-1 and k != n-2:
            test(i,k+1)
        elif l == n-1 and k == n-2:
            if i == n-4:
                test(i+1,k)
            elif i < n-4:
                test(i+1,k-1)

i = 0
k = i+1
test(i,k)

print(b)

dem = 0
for j in a:
    m = b.count(float(j))
    if m != 0:
        dem += 1

print(dem)