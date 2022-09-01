# Task_2
date_sec = int(input('Enter seconds: ', ))

date_min = date_sec / 60
date_hour = date_sec / 3600
print(f'{date_hour}:{date_min}:{date_sec}')


# Task_3
n = int(input('Enter number: ', ))

total = n + (n * 11) + (n * 111)
print(total)


# Task_4
numb = int(input('Enter number: ', ))

i = 0
while numb > 0:
    last = numb % 10
    if last >= i: i = last
    numb = numb // 10
print('Max number: ', i)


# Task_5
numb_1 = int(input('Enter income: ', ))
numb_2 = int(input('Enter costs: ', ))

if numb_1 > numb_2:
    print ('Profit')
else:
    print ('Need to work harder')


# Task_6
numb_1 = int(input('Enter income: ', ))
numb_2 = int(input('Enter costs: ', ))

if numb_1 > numb_2:
    profit = (numb_1 / numb_2)
    numb_3 = int(input('Enter employees: ', ))
    profit_for_one = profit / numb_3
    print('Profit per employee: ', profit_for_one)
else:
    print('Need to work harder')


# Task_7
start_dis = 2
final_dis = 3

days = 1
while final_dis >= start_dis:
    start_dis = start_dis * 1.1
    days = days + 1
print(f'On the {days}th day')
