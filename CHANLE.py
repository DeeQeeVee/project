#open file input and output
file_input = open("CHANLE.inp", "r")
file_output = open("CHANLE.out", "w")

#get elemnet from file input
a, b = file_input.readline().split()

#convert string to int
a = int(a)
b = int(b)

i = 1
sqrt_b = b ** 0.5
if_a, if_b = True, True
location, element = 0, 0
count = [0]

while if_a or if_b:
        i += 1
        count.append(count[i - 1] + 1)

        if sqrt_b - 1 == 0:
                location = count[i]

                if_b = False

        if 0 < sqrt_b < 1:
                if b % 2 == (i + 1) % 2:
                        location = count[i - 1] + int((b - (i - 1) ** 2 + 1) / 2) + 1
                
                else:
                        