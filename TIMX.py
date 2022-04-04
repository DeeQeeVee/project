file_input = open("TIMX.inp", "r")
file_output = open("TIMX.out", "w")

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

n = int(file_input.readline())
F = list(map(int, file_input.read().split()))
F = quick_sort(F)

if n % 2 == 1:
        print(F[n // 2], file = file_output)
else:
        a, b = F[n // 2 - 1] , F[n // 2]

        for i in range(a, b + 1):
                print(i, end = " ",file=file_output)