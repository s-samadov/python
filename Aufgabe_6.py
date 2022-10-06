# Task_1

from time import sleep

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()


# Task_2

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume

r = MassCount(25, 10000, 125)
print(r.mass())



# Task_3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
        # return f'{sum(self._income.values())}'


a = Position('Saidaziz', 'Samadov', 'DevOps', 100000, 25000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())


# Task_4


# Task_5

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Start rendering {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. Start rendering {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'ВYou took {self.title}. Start rendering {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}. Start rendering {self.title}'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())