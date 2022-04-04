file_input = open("CUCDAI.inp", "r")
file_output = open("CUCDAI.out", "w")

n = file_input.readline()
n = int(n)

l_fst = file_input.readline().split()
l = []
for i in l_fst:
        l.append(int(i))

total = 0
for i in range(len(l) - 1):
        if (l[i - len(l) + 1] < l[i]) and (l[i - len(l) - 1] < l[i]):
                total += 1
                
print(total, file = file_output)