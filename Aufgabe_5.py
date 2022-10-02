# Task_1

# f = open('test.txt', 'w')
# line = input('Enter text: ')
# while True:
#     f.writelines(line)
#     line = input('Enter text: ')
#     if line == 'q':
#         break
# f.close()

# Task_2

# f = open(r'C:\Users\4Fun4959\PycharmProjects\erste\test.txt')
# l = 0
# w = 0
# for line in f:
#     l = l + 1
#     w = w + len(line.split())
# print(l)
# print(w)


# Task_3

# f = open(r'C:\Users\4Fun4959\PycharmProjects\erste\test.txt')
# w = []
# s = []
# l = f.read().split('\n')
# for i in l:
#     i = i.split()
#     if int(i[1]) < 20000:
#         w.append(i[0])
#     s.append(i[1])
#     mid = sum(map(int, s)) / len(s)
# print(f'Оклад меньше 20.000 {w}, средний оклад {mid}')


# Task_4

# tran = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# n_tab = []
#
# with open(r'C:\Users\4Fun4959\PycharmProjects\erste\test.txt') as file:
#     for i in file:
#         i = i.split(' ', 1)
#         n_tab.append(tran[i[0]] + '  ' + i[1])
#     print(n_tab)
#
# with open('test_2.txt', 'w', encoding="utf-8") as file_2:
#     file_2.writelines(n_tab)


# Task_5

# with open('test_3.txt', 'w+') as file:
#     line = input('Enter numbers: ')
#     file.writelines(line)
#     numb = line.split()
#     print(sum(map(int, numb)))


# Task_6

# subjects = {}
# with open(r'C:\Users\4Fun4959\PycharmProjects\erste\test_4.txt', encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         data = line.replace('(', ' ').split()
#         subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
# print(subjects)


# Task_7
