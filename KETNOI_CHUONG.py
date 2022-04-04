file_input = open("KETNOI.inp", "r")
file_output = open("KETNOI.out", "w")

n, m = file_input.read().split("\n")
m = m.split()

def qs(m):
    if len(m) < 2:
        return m
    k = m[0]
    L = [i for i in m[1:] if (i + k) >= (k + i)]
    R = [i for i in m[1:] if (i + k) < (k + i)]
    return qs (L) + [k]+ qs(R)

print(qs(m), file = file_output)

file_input.close()
file_output.close()