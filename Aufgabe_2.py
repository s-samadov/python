# Task_1
ls = ['omg', 4, 4.1, [1,2,3]]
for val in ls:
    print(type(val))


# Task_2
ls = input('Enter value: ', ).split()
print(ls)
ls[:-1:2], ls[1::2] = ls[1::2], ls[:-1:2]
print(ls)


# Task_3
month = int(input('Enter month: ', ))
cal = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
for val in cal:
    if month in cal[val]:
        print(val)
        break

month = int(input('Enter month: ', ))
if month in [12, 1, 2]:
    print('Winter')
elif month in [3, 4, 5]:
    print('Spring')
elif month in [6, 7, 8]:
    print('Summer')
else:
    print('Autumn')


# Task_4
my_str = input('Enter: ', ).split()
for numb, word in enumerate(my_str, 1):
    if len(word) <= 10:
        print(f'{numb}. {word}')
    else:
        print(f'{numb}. {word[0:10] }')


# Task_5
my_list = [7, 5, 3, 3, 2]
numb = int(input('Enter number: ', ))
yes_no = my_list.count(numb)
for val in my_list:
    if yes_no == 1:
        place = my_list.index(numb)
        my_list.insert(place + yes_no, numb)
        break
    else:
        if numb > val:
            l_place = my_list.index(val)
            my_list.insert(l_place, numb)
            break
        else:
            my_list.append(numb)
            break
print(my_list)


# Task_6
main_qty = 0
my_staff = []
my_dict = {}
analitics = {}
while True:
    main_qty = main_qty + 1
    name = input("Enter Name: ")
    my_dict['Name'] = name
    price = input("Enter Price: ")
    my_dict['Price'] = price
    qty = input("Enter Quantity: ")
    my_dict['Quantity'] = qty
    unit = input("Enter Unit: ")
    my_dict['Unit'] = unit
    my_staff.append(tuple([main_qty, my_dict]))
    print(my_staff)
    finish = input('is the list ready? (y/n)) ')
    if finish.lower() == 'y':
        break
