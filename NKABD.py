file_input = open("NKABD.inp", "r")
file_output = open("NKABD.out", "w")

l1 = file_input.readline().split()
l, r = int(l1[0]), int(l1[1])

total = [1]*(r + 1)

for i in range(2, (r // 2) + 1):
        for j in range(2, (r // i) + 1):
                total[i * j] += i

teemo = 0

for i in range(l, r + 1):
        if (total[i] > i):
                teemo += 1

print(teemo, file = file_output)