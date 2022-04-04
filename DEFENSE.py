file_input = open("DEFENSE.inp", "r")
file_output = open("DEFENSE.out", "w")

n = file_input.readline()
n = int(n)
teemo = file_input.readline().split()
a = []
for i in teemo:
    a.append(int(i))

result = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and result[j] + 1 > result[i]:
            result[i] = result[j] + 1

print(max(result), file = file_output)