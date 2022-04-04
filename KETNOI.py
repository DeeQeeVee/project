with open("KETNOI.inp", "r") as file_input:
        n = int(file_input.readline())
        l = list(map(int, file_input.read().split()))
        a = [0] * 100

with open("KETNOI.out", "w") as file_output:
        for i in range(n):
                a[l[i]] = a[l[i]] + 1

        for i in range(99, 9, -1):
                x = i // 10
                y = i % 10

                while (a[x] > 0) and (x > y):
                        file_output.write(str(x))
                        a[x] = a[x] - 1
                        
                while (a[i] > 0):
                        file_output.write(str(i))
                        a[i] = a[i] - 1