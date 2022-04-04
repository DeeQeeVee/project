file_input = open("TWINS.inp", "r")
file_output = open("TWINS.out", "w")
x, y = file_input.read().split()
x, y = int(x), int(y)


def snt(n, m):
        xet = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
                if xet[i]:
                        for j in range(i * i, n + 1, i):
                                xet[j] = False

        d = 0
        if m < n:
                for i in range(2, n + 1 - m):
                        if xet[i] and xet[i + m]:
                                d = d + 1
        return d


print(snt(x, y), file = file_output)