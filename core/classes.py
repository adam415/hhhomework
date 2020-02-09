class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return "{{brand: '{}', model: '{}'}}".format(self.brand, self.model)


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars = []):
        self.cars = cars
    
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index):
        return self.cars[index]

    def __repr__(self):
        return repr(self.cars)

    def add(self, car):
        self.cars.append(car)

    def delete(self, index):
        del self.cars[index]


g = Garage([
    Car('B1', 'M1'),
    Car('B2', 'M2'),
    Car('B3', 'M3')
])

print('print(g): ')
print(g)

print('iterate over g: ')
for c in g:
    print(c)


print('after add and delete: ')

g.add(Car('B4', 'C4'))
g.add(Car('B5', 'C5'))
g.delete(2)

print(g)