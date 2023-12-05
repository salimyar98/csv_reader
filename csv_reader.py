import csv
import re
from tabulate import tabulate

data = input('Введите путь к файлу: ')
with open(data) as f:
    lines = csv.reader(f)
    headers = next(lines)
    lines = list(lines)

dict_str = {i[0]: i for i in lines}


def arguments(tmp, dict_str, headers, num):
    arg = dict_str.get(re.sub("[^0-9]", "", tmp[num]), [])
    return int(arg[headers.index(re.sub("[^A-Za-z]", "", tmp[num]))])


for (n, i) in enumerate(lines):
    for (b, m) in enumerate(i):
        if m.startswith('='):
            operators = ['+', '-', '/', '*']
            operator = next((j for j in operators if j in m), None)
            if operator:
                tmp = m.split(operator)
                arg_a = arguments(tmp, dict_str, headers, 0)
                arg_b = arguments(tmp, dict_str, headers, 1)
                match operator:
                    case '+':
                        result = arg_a + arg_b
                    case '-':
                        result = arg_a - arg_b
                    case '/':
                        if arg_b != '0':
                            result = arg_a / arg_b
                    case '*':
                        result = arg_a * arg_b
                i[b] = result

line_print = {str(n): i for n, i in enumerate(lines)}
print(tabulate(line_print.values(), headers=headers, tablefmt="grid"))
input('Нажмите "Enter" для выхода.')
