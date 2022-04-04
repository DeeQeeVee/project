def quick_sort(list):   
        length = len(list)

        if length <= 1:
                return list

        mid = list.pop()
        greater = []
        lower = []

        for item in list:

                if item > mid:
                        greater.append(item)

                else:
                        lower.append(item) 
        return quick_sort(lower) + [mid] + quick_sort(greater)

file_input = open("PHUDOAN.inp", "r")
file_output = open("PHUDOAN.out", "w")

n = int(file_input.readline())
F = []

for line in file_input:
        a, b = map(int,line.split())
        F.append([a, a + b])

F = quick_sort(F)
s = F[n - 1][1] - F[0][0]
a = 0

print(s)

for i in range(1, n):
        if F[i][0] <= F[i - 1][1]:
                F[i][0] = F[i - 1][0]
                if F[i][1] < F[i - 1][1]:
                        F[i][1] = F[i - 1][1]

        else:
                a += F[i - 1][1] -F[i - 1][0]
                s -= F[i][0] - F[i - 1][1]
                print(a)

print(F)
print(s, file = file_output)