file_input = open("ROBOT.inp", "r")
file_output = open("ROBOT.out", "w")

m, n = map(int, file_input.readline().split())
n += 1
m += 1
F = [[0] * n]
A = [[0] * n]
i = 0

for line in file_input:
        i += 1
        F.append([0] + list(map(int, line.split())))
        A.append(F[i].copy())

for i in range(1, m):
        for j in range(1, n):
                F[i][j] = 2 * max(F[i - 1][j], F[i][j - 1]) + A[i][j]
                
print(F[i][j], file = file_output)