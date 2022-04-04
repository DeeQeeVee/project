file_input = open("TAXI.inp", "r")
file_output = open("TAXI.out", "w")

n = int(file_input.readline())
P = list(map(int, file_input.read().split()))

l1 = [0]*5

for i in P:
        l1[i] += 1

teemo = l1[4] + l1[3]

if (l1[1] > l1[3]): 
        l1[1] -= l1[3]
        teemo += l1[2]

        if (l1[1] - l1[2]*2 > 0):
                l1[1] -= l1[2]*2
                teemo += l1[1]// 4

                if (l1[1] % 4 > 0):
                        teemo += 1
     
else: 
        l1[1] = 0
        teemo += (l1[2]*2) // 4

        if  ((l1[2]*2) % 4 > 0):
                teemo += 1

print(teemo, file = file_output)