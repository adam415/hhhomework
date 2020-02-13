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
gen3 = (randint(1, 100) for _ in range(1, N + 1))

g1 = gen(10)
print('gen', g1) # печатают <generator ...>, так что мы знаем, что это действительно генератор, а не сразу коллекция
for r in g1:
    print(r)

g2 = gen2(10)
print('gen2', g2)
for r in g2:
    print(r)

print('gen3', gen3)
for r in gen3:
    print(r)