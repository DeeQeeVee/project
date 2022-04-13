file_input = open("CHL.inp", "r")
file_output = open("CHL.out", "w")

n, k = map(int, file_input.readline().split())

cn = 1
ck = 1
cnk = 1

def cnk(x, y):

        global cn, ck, cnk
        for i in range(2, n + 1):
                cn *= i
                if (i == y):
                        ck = cn

                if (i == x - y):
                        cnk = cn

        cnk = cn / (ck * cnk)
        return cnk

print(int(cnk(n, k)), file = file_output, end = "")