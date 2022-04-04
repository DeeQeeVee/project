file_input = open("DAYF.inp", "r")
file_output = open("DAYF.out", "w")

for line in file_input:
    x, y = line.split()
    n = int(x)
    k = int(y)

def fibo(k, n):
    d = []
    f0 = 1
    f1 = 1
    fn = 2
    
    if k == 0 or k == 1:
        return 1
    elif k >=2 and k < 11:
        for i in range(2, k):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn

    elif k >= 11:
        d.append(f0)
        d.append(f1)
        d.append(fn)
        for i in range(2, n + 1):
            f0 = f1
            f1 = fn
            fn = f0 + f1
            fn = fn % 128
            d.append(fn)
        d.sort()
        return d[k]

print(fibo(k, n), file = file_output)
