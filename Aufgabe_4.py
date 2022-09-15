# Task_1

from sys import argv
path, time, rate, bonus = argv
time, rate, bonus = map(int, argv[1:])
salary = time * rate + bonus
print(f'Salary: {salary}')


# Task_2

ls_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
ls_2 = [ls_1[i] for i in range(1, len(ls_1)) if ls_1[i-1] <ls_1[i]]
print(f'Old list {ls_1}')
print(f'New list {ls_2}')


# Task_3

gen_1 = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(gen_1)


# Task_4

ls_o = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
ls_n = [i for i in ls_o if ls_o.count(i) == 1]
print(ls_n)


# Task_5

from functools import reduce
gen_2 = [i for i in range(100, 1001) if i % 2 == 0]
sum_all = reduce(lambda x, y: x * y, gen_2)
print(sum_all)


# Task_6

from itertools import count
for el in count(int(input('Enter number: ', ))):
    if el == 100:
        break
    print(el)

from itertools import cycle
ls = ['omg', 4, 4.1, [1,2,3]]
count = 0
for el_2 in cycle(ls):
    count = count + 1
    if count == 10:
        break
    print(el_2)


# Task_7

# Непонял задачу
