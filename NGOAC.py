#open file input and output
file_input = open("NGOAC.inp", "r")
file_output = open("NGOAC.out", "w")

string = file_input.read()
end_string = len(string)

count = 0
test = 0
demo = 0
for i in string:
        if test == 0:
                if i == "(":
                        count += 1
                elif i == ")":
                        count -= 1
                        if count < 0:
                                test += 1

        if i not in ["(", ")"]: 
                print("KHONG HOP LE", file = file_output)
                demo += 1
                break

if demo  == 0:
        if count == 0:
                print("HOP LE", file = file_output)
        else:
                print("KHONG HOP LE", file = file_output)