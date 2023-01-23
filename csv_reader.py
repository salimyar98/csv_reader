import csv
import re
from tabulate import tabulate

data = input('Введите путь к файлу: ')
with open(data) as f:
    lines = csv.reader(f)
    headers = next(lines)
    lines = list(lines)

dic_str = {}

for i in lines:
    n = 0
    tmp = dict.fromkeys([i[n]], i)
    n += 1
    dic_str.update(tmp)

for (n, i) in enumerate(lines):
    for (b, m) in enumerate(i):
        if m.startswith('='):
            if '+' in m:
                tmp = m.split('+')
                tmp_head = re.sub("[^A-Za-z]", "", tmp[0])
                tmp_str = str(re.sub("[^0-9]", "", tmp[0]))
                tmp_head = headers.index(tmp_head)
                arg_a = dic_str[tmp_str][tmp_head]
                
                tmp_head_2 = re.sub("[^A-Za-z]", "", tmp[1])
                tmp_str_2 = str(re.sub("[^0-9]", "", tmp[1]))
                tmp_head_2 = headers.index(tmp_head_2)
                arg_b = dic_str[tmp_str_2][tmp_head_2]
                result = int(arg_a) + int(arg_b)
                
                i.pop(b)
                i.insert(b, result)
                
            if '-' in m:
                tmp = m.split('-')
                tmp_head = re.sub("[^A-Za-z]", "", tmp[0])
                tmp_str = str(re.sub("[^0-9]", "", tmp[0]))
                tmp_head = headers.index(tmp_head)
                arg_a = dic_str[tmp_str][tmp_head]
                
                tmp_head_2 = re.sub("[^A-Za-z]", "", tmp[1])
                tmp_str_2 = str(re.sub("[^0-9]", "", tmp[1]))
                tmp_head_2 = headers.index(tmp_head_2)
                arg_b = dic_str[tmp_str_2][tmp_head_2]
                result = int(arg_a) - int(arg_b)
                
                i.pop(b)
                i.insert(b, result)
            if '/' in m:
                tmp = m.split('/')
                tmp_head = re.sub("[^A-Za-z]", "", tmp[0])
                tmp_str = str(re.sub("[^0-9]", "", tmp[0]))
                tmp_head = headers.index(tmp_head)
                arg_a = dic_str[tmp_str][tmp_head]
                
                tmp_head_2 = re.sub("[^A-Za-z]", "", tmp[1])
                tmp_str_2 = str(re.sub("[^0-9]", "", tmp[1]))
                tmp_head_2 = headers.index(tmp_head_2)
                arg_b = dic_str[tmp_str_2][tmp_head_2]
                if arg_b != '0':
                    result = int(arg_a) / int(arg_b)
                    i.pop(b)
                    i.insert(b, result)
            if '*' in m:
                tmp = m.split('*')
                tmp_head = re.sub("[^A-Za-z]", "", tmp[0])
                tmp_str = str(re.sub("[^0-9]", "", tmp[0]))
                tmp_head = headers.index(tmp_head)
                arg_a = dic_str[tmp_str][tmp_head]
                
                tmp_head_2 = re.sub("[^A-Za-z]", "", tmp[1])
                tmp_str_2 = str(re.sub("[^0-9]", "", tmp[1]))
                tmp_head_2 = headers.index(tmp_head_2)
                arg_b = dic_str[tmp_str_2][tmp_head_2]
                result = int(arg_a) * int(arg_b)
                
                i.pop(b)
                i.insert(b, result)

line_print = {}
n = '0'
for i in lines:
    tmp_dict = dict.fromkeys(n, i)
    n = int(n) + 1
    n = str(n)
    line_print.update(tmp_dict)

print(tabulate(line_print.values(), headers=headers, tablefmt="grid"))
input('Нажмите "Enter" для выхода.')