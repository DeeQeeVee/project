file_input = open("SUMQUERIES.inp", "r")
file_output = open("SUMQUERIES.out", "w")

N, Q = map(int, file_input.readline().split())
Fn = list(map(int, file_input.readline().split()))

for i in range(1, N):
        Fn[i] += Fn[i - 1]

for line in file_input:

        i, r = map(int, line.split())

        if i - 2 < 0:
                k = 0

        else:
                k = Fn[i - 2]
                
        print(Fn[r - 1] - k, file=file_output)