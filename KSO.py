file_input = open("KSO.inp", "r")
file_output = open("KSO.out", "w")

l = file_input.read().split()
m, n, k = int(l[0]), int(l[1]), int(l[2])

if k > 0:
    x = pow(m, n, 10**k)

    if x == 0:
        print("0"*k, file = file_output)

    else:
        if x < 10**(k - 1):
            print("0", x, sep = "", file = file_output)
            
        else:
            print(x, file = file_output)
    