file_input = open("KITUCHUNG.inp", "r")
file_output = open("KITUCHUNG.out", "w")

x = file_input.readline()
y = file_input.readline()

count1 = {}
count2 = {}

for j in range(97, 123):
        i = chr(j)
        count1[i] = False
        count2[i] = False

for i in x:
        count1[i] = True

for i in y:
        count2[i] = True

for i in count1:
        if i != "\n" and count1[i] and count2[i]:
                print(i, file = file_output)