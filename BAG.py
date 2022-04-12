file_input = open("BAG.inp","r")
file_output = open("BAG.out","w")

a1 = file_input.readline().split()
n1 = int(a1[0])
n2 = int(a1[1])

w = []
v = []

for i in range(n1):
    a2 = file_input.readline().split()
    w.append(int(a2[0]))
    v.append(int(a2[1]))

d1 = [] 
f = []
max1 = []

for i in range(n1 + 1):
    for j in range(n2 + 1):

        if i == 0 or j == 0:
            d1.append(0)

        else:

            if j - w[i - 1] >= 0:
                if f[i - 1][j - w[i - 1]] + v[i - 1] > f[i - 1][j]:
                    d1.append(f[i - 1][j - w[i - 1]] + v[i - 1])

                else:
                    d1.append(f[i - 1][j])

            else:
                d1.append(0)
    f.append(d1)
    max1.append(max(d1))
    d1 = []

print(max(max1), file = file_output, end = "")