#open file input and output
file_input = open("demo.inp", "r")
file_output = open("demo.out", "w")

x, y= file_input.read().split()
a = []

x_max, y_max = len(x), len(y)
str_max = max(x_max, y_max)
total = 0

a = [0] * str_max

def main(n, m):
        global x_max, y_max, total

        for i in range(x_max):
                demo = 0

                for j in range(y_max):
                        t = a[j]

                        if m[i] == n[j]:
                                a[j] = demo + 1
                        
                        else:
                                a[j] = 0
                        
                        total = max(total, a[j])
                        
                        demo = t
        return total

print(main(x, y), file = file_output)