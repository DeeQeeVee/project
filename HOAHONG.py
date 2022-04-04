file_input = open("HOAHONG.inp", "r")
file_output = open("HOAHONG.out", "w")

min, max = map(int, file_input.readline().split())
demo = ["7", "9"]

count = 0

for i in demo:

        if min <= int(i) <= max:
                count += 1

d, c = 0, len(demo)

while int(demo[c-1]) <= max:

        for i in range(d,c):

                if min <= int("7"+ demo[i]) <= max:
                        count += 1

                if int("7" + demo[i]) > max:
                        c = 0
                        break 

        demo.append("7"+ demo[i])

        if c == 0: 
                break

        for i in range(d,c):
                
                if  min <= int("9"+ demo[i]) <= max:
                        count += 1

                if  int("9" + demo[i]) > max:
                        c = 0
                        break 

        demo.append("9"+ demo[i])

        if c == 0: 
                break
        
        d, c = c, len(demo)

print(count, file = file_output)