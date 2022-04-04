#Create file input and output
file_input = open("NHUAN.inp", "r")
file_output = open("NHUAN.out", "w")

#Read input and convert string to number
n = file_input.read()
n = int(n)

#Body
if (n >= 1900) and (n <= 2100):
        if (n % 4 == 0) and (n % 100 != 0):
                print("YES", file = file_output)
        else:
                print("NO", file = file_output)