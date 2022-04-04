file_input = open("XOAK.inp", "r")
file_output = open("XOAK.out", "w")

n, k = map(int, file_input.readline().split())
s = ""

for i in range(1, n + 1):
        s += str(i)

if k >= len(s):
        s = ""

else:
        if k <= 8:
                s = s[k:]

        else:
                s = s[8:]
                k -= 8
                n = len(s) - 2
                i = 0

                while i <= n and k != 0:

                        if s[i] < s[i + 1]:
                                if i == 0:
                                        s = s[i + 1:]

                                else:
                                        s = s[:i] + s[i + 1:]

                                k -= 1
                                n -= 1
                                i -= 1

                        else:
                                i += 1

                if k > 0:
                        s = s[:len(s) - k]

print(s, file = file_output)