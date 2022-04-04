from math import gcd

file_input = open("PHANSO.inp", "r")
file_output = open("PHANSO.out", "w")

n, k = map(int, file_input.readline().split())

F = [[0, 1], [1, 1]]

for i in range(2, n + 1):

        for j in range(1, i):

                if gcd(i, j) == 1:
                        F.append([j, i])

def quick_sort(list):
        length = len(list)

        if length <= 1:
                return list

        mid = list.pop()
        greater = []
        lower = []

        for item in list:
                if item[0]/item[1] > mid[0]/mid[1]:
                        greater.append(item)

                else:
                        lower.append(item)

        return quick_sort(lower) + [mid] + quick_sort(greater)

F = quick_sort(F)
print(*F[k - 1], file=file_output)
