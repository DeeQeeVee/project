file_input = open("CHANLE.inp", "r")
file_output = open("CHANLE.out", "w")

n = file_input.readline()
n = int(n)
demo = file_input.readline().split()
demo = [int(i) for i in demo]
total = -1


for i in range(1, n):
        if demo[i - 1] % 2 != demo[i] % 2:
                total = max(total, demo[i] + demo[i - 1])

print(total, file = file_output)