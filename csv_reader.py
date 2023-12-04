import csv
import re
from tabulate import tabulate

data = input('Введите путь к файлу: ')
with open(data) as f:
    lines = csv.reader(f)
    headers = next(lines)
    lines = list(lines)

dic_str = {i[0]: i for i in lines}

for (n, i) in enumerate(lines):
    for (b, m) in enumerate(i):
        match m:
            case m if m.startswith('=') and '+' in m:
                tmp = m.split('+')
                arg_a = dic_str[re.sub("[^0-9]", "", tmp[0])][headers.index(re.sub("[^A-Za-z]", "", tmp[0]))]
                arg_b = dic_str[re.sub("[^0-9]", "", tmp[1])][headers.index(re.sub("[^A-Za-z]", "", tmp[1]))]
                result = int(arg_a) + int(arg_b)
                i[b] = result
            
            case m if m.startswith('=') and '-' in m:
                tmp = m.split('-')
                arg_a = dic_str[re.sub("[^0-9]", "", tmp[0])][headers.index(re.sub("[^A-Za-z]", "", tmp[0]))]
                arg_b = dic_str[re.sub("[^0-9]", "", tmp[1])][headers.index(re.sub("[^A-Za-z]", "", tmp[1]))]
                result = int(arg_a) - int(arg_b)
                i[b] = result
            
            case m if m.startswith('=') and '/' in m:
                tmp = m.split('/')
                arg_a = dic_str[re.sub("[^0-9]", "", tmp[0])][headers.index(re.sub("[^A-Za-z]", "", tmp[0]))]
                arg_b = dic_str[re.sub("[^0-9]", "", tmp[1])][headers.index(re.sub("[^A-Za-z]", "", tmp[1]))]
                if arg_b != '0':
                    result = int(arg_a) / int(arg_b)
                    i[b] = result
            
            case m if m.startswith('=') and '*' in m:
                tmp = m.split('*')
                arg_a = dic_str[re.sub("[^0-9]", "", tmp[0])][headers.index(re.sub("[^A-Za-z]", "", tmp[0]))]
                arg_b = dic_str[re.sub("[^0-9]", "", tmp[1])][headers.index(re.sub("[^A-Za-z]", "", tmp[1]))]
                result = int(arg_a) * int(arg_b)
                i[b] = result

line_print = {str(n): i for n, i in enumerate(lines)}
print(tabulate(line_print.values(), headers=headers, tablefmt="grid"))
input('Нажмите "Enter" для выхода.')
