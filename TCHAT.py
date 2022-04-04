file_input = open("TCHAT.inp", "r")
file_output = open("TCHAT.out", "w")

n = file_input.read()
n = int(n)

if (n % 2 == 0) and (n % 7 == 0):
        print("CO", file = file_output)
else:
        print("KHONG", file = file_output)