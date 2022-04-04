file_input = open("QBMAX.inp", "r")
file_output = open("QBMAX.out", "w")

m, n = map(int, file_input.readline().split())
n += 1
F = [[0] * n]

for line in file_input:
        F.append([0] + list(map(int, line.split())))

F.append([0] * n)
ma = F[1][0] + F[1][1]
m += 1

for j in range(1, n):
        for i in range(1, m):
                F[i][j] = max(F[i][j - 1], F[i - 1][j - 1], F[i + 1][j - 1]) + F[i][j]

                if F[i][j] > ma:
                        ma = F[i][j]

print(ma, file = file_output)