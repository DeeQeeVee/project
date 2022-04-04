file_input = open("TICHMAX.inp", "r")
file_output = open("TICHMAX.out", "w")

n = file_input.readline()
a = file_input.readline().split()

for i in range(len(a)):
    a[i] = int(a[i])
a.sort()

count = a[-1] * a[-2] * a[-3]
if a[0] * a[1] > 0:
    if a[0] * a[1] * a[-1] > a[-1] * a[-2] * a[-3]:
        count = a[0] * a[1] * a[-1]

print(count, file = file_output)