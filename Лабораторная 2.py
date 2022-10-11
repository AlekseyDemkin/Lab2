import csv
import os

RED = "\u001b[41m"
BLUE = "\u001b[44m"
WHITE = "\u001b[47m"
END = "\u001b[0m"
d = 24
for i in range(6):
    if i == 0 or i == 5:
        print(RED + " " * d + END)
    elif i == 1 or i == 4:
        print(WHITE + " " * d + END)
    else:
        print(BLUE + " " * d + END)
n = int(input("Введите кол-во повторений узора:"))
print((" " * 9 + WHITE + " " * 2 + END + " " * 9 + END) * n)
print((" " * 8 + WHITE + " " * 1 + END + " " * 2 + END + WHITE + " " * 1 + END + " " * 8 + END) * n)
print((" " * 6 + WHITE + " " * 2 + END + " " * 4 + END + WHITE + " " * 2 + END + " " * 6 + END) * n)
print((" " * 3 + WHITE + " " * 3 + END + " " * 8 + END + WHITE + " " * 3 + END + " " * 3 + END) * n)
print((WHITE + " " * 4 + END + " " * 12 + END + WHITE + " " * 4 + END) * n)


def esc(code):
    return f'\u001b[{code}m'


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
END = esc(0)

array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

# flag_cz()

for i in range(1, 10):
    result[i] = 1 / i
print(result)

step = abs((result[9] - result[1])) / 9

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

count = 0
count_b = 0
count_m = 0
with open("books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    for row in list(table)[1:]:
        if int(row[7][:-3]) > 50:
            count_b += 1
        else:
            count_m += 1
count = count_b + count_m
pr = count / 100
print()
print("Книги до 50 рублей и дороже:")
print(RED + "  " + END + "- Дороже 50 рублей" + " " + BLUE + "  " + END + "- Дешевле 50 рублей")
print()
print(round(count_m / pr, 1), "%", BLUE + " " * round(count_m / pr) + END)
print()
print(round(count_b / pr, 1), "%", RED + " " * round(count_b / pr) + END)
os.system("cls")