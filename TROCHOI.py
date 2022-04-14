file_input = open("TROCHOI.inp", "r")
file_output = open("TROCHOI.out", "w")

m, n = map(int, file_input.readline().split())
l = list(map(int, file_input.readline().split()))

#sort list
l.sort()
l = [l[i:i + n] for i in range(0, len(l), n)]

for i in range(len(l)):
        if i % 2 == 0:
                print(*l[i], file = file_output)

        if i % 2 != 0:
                l[i] = l[i][::-1]
                print(*l[i], file = file_output)