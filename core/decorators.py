def cache_decorator(func):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    cache = {}

    def caller(*args, **kwargs):
        key = (*args, *kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)
        else:
            print('Hi, it\'s @cache_decorator. Have your value from my cache. See you.')
            
        return cache[key]
    
    return caller