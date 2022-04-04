#Create new file and open it
file_input = open("KARAOKE.inp", "r")
file_output = open("KARAOKE.out", "w")

#Create new variable, insert data from file to variable and convert it to number
day = file_input.readline()
demo = file_input.readline().split()

day = int(day)
start = int(demo[0])
end = int(demo[1])
time = end - start

#Create new variable
result = 0

#Calculating...

#Saturday and Sunday
if (day in [7, 8]):
        result = time*60000

#From Monday to Friday
else:
        result, total, count = 0, 0, 0
        for i in range(start + 1, end + 1):
                count += 1
                if (count > 3):
                        if (i <= 14):
                                total += 28000

                        else:
                                total += 35000
                
                else:
                        if (i <= 14):
                                result += 40000
                        
                        else:
                                result += 50000
        
        result = result + total
#Print result
print(int(result), file = file_output)