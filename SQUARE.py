file_input = open("SQUARE.inp", "r")
file_output = open("SQUARE.out", "w")
file_input.readline()
x_max, x_min, y_max, y_min = 1, 100, 1, 100

for line in file_input:
        x, y = map(int, line.split())

        x_max = max(x_max, x)
        x_min = min(x_min, x)
        y_max = max(y_max, y)
        y_min = min(y_min, y)

print(max(x_max - x_min, y_max - y_min) ** 2, file = file_output)