from random import randint

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
# Через цикл
def gen(N):
    for _ in range(1, N + 1):
        yield randint(1, 100)

# Через comprehension
def gen2(N):
    return (randint(1, 100) for _ in range(1, N + 1))

# написать генераторное выражение, которое делает то же самое
N = 10
already_generated = [randint(1, 100) for _ in range(1, N + 1)]

print('gen')
for r in gen(10):
    print(r)

print('gen2')
# print(gen2(10)) - печатает <generator ...>, так что мы знаем, что это действительно генератор, а не сразу коллекция
for r in gen2(10):
    print(r)

print('already_generated')
for r in already_generated:
    print(r)