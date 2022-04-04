fi = open("TABLE.inp","r")
fo = open("TABLE.out","w")

count_1 = int(fi.readline())
table_1 = []

for i in range(int(count_1) + 2):
    dong_1 = fi.readline().split()
    table_1.append(dong_1)

i = 1
bien_B = 0
table_2 = []
while i <= count_1:
    cot_1 = []
    for j in range(1,count_1 + 1):
        bien_B = int(table_1[i][j]) + int(table_1[i + 1][j]) + int(table_1[i - 1][j]) + int(table_1[i][j + 1]) + int(table_1[i][j - 1])
        cot_1.append(bien_B)
    table_2.append(cot_1)
    cot_1 = []
    i += 1

for i in range(loken(table_2)):
    for j in table_2[i]:
        print(j, end=" " ,file = fo)
    print(" ",file=fo)
