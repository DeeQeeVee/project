file_input = open("HVC.inp", "r")
file_output = open("HVC.out", "w")

n, k = map(int, file_input.readline().split())

#read list of list in file_input
l = []
for i in range(n):
        l.append(list(map(int, file_input.readline().split())))

#add 0 first column
for i in range(n):
        l[i].insert(0, 0)

#add 0 in first raw
l.insert(0, [0]*(n + 1))

total = 0

for i in range(1, n + 1):
        for j in range(1, n + 1):
                l[i][j] += l[i - 1][j] + l[i][j - 1] - l[i - 1][j - 1]

for i in range(k, n + 1):
        for j in range(k, n + 1):
                total = max(total, l[i][j] - l[i][j - k] - l[i - k][j] + l[i - k][j - k])

print(total, file = file_output, end = "")