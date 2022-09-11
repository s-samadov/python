# Task_1
def f1():
    try:
        a = int(input('Enter numb1: '))
        b = int(input('Enter numb2: '))
        res = a / b
    except ZeroDivisionError:
        return 'Error'
    return res
print(f1())


# Task_2
name = input('Enter Name: ')
surname = input('Enter Surname: ')
year = int(input('Enter Year: '))
city = input('Enter City: ')
email = input('Enter Email: ')
phone = int(input('Enter Phone: '))
def f2():
      return(f'name: {name}, surname: {surname}, year: {year}, city: {city}, email: {email}, phone: {phone}')
print(f2())


# Task_3
def my_func():
    ls = []
    a = int(input('Enter number:'))
    ls.append(a)
    b = int(input('Enter number:'))
    ls.append(b)
    c = int(input('Enter number:'))
    ls.append(c)
    ls.sort()
    s = ls[1] + ls[2]
    print(ls)
    return s
print(my_func())


# Task_4
def my_func(x, y):
    res = x ** y
    return res
print(my_func(int(input("x: ")), int(input("y: "))))

def my_func(x, y):
    res = 1
    while y > 0:
        res = res * x
        y = y - 1
    return res
print(my_func(int(input("x: ")), int(input("y: "))))


# Task_5
def f5():
    Total = 0
    while True:
        numbs = input('Enter numb / q  ', ).lower().split()
        for n in numbs:
            if n == 'q':
                return
            else:
                Total = Total + int(n)
        print(Total)
f5()


# Task_6 and Task_7
def int_func():
    text =  str(input('Enter text: ')).title()
    print(text)
int_func()
