file_input = open("KETNOI.inp", "r")
file_output = open("KETNOI.out", "w")

a = file_input.readline().split()
n = int(a[0])
del(a[0])
a.sort()
a = a[::-1]

s = ""

for i in a:
    s += i
if len(s) <= 20:
    print(len(s), "[", s, "]", end = "", file = file_output)
else:
    print(len(s), "[", s[0:10], "...",s[len(s) - 10 : len(s)], "]", end = "", file = file_output)