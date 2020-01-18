from decorators import cache_decorator

def allAreOneOf(vals, types):
    return all(isinstance(val, types) for val in vals)

def inputNum():
    # В итоге мне показалось, что отловить исключение проще, чем по регулярке проверять
    while True:
        inp = input('Введите десятичное число: ')

        try:
            result = float(inp)
            break
        except:
            print('Не удалось распознать введенное число :(')
    
    return result

def calculator(a, b, operation):
    if not allAreOneOf((a, b), (int, float, complex)):
        return 'Invalid operands'
    if operation not in calculator.__operations__:
        return 'Invalid operation'

    if operation in ['/', '//', '%'] and b == 0:
        return 'Undefined result'
    if operation == '%' and (isinstance(a, complex) or isinstance(b, complex)):
        return 'Undefined result'

    return calculator.__operations__[operation](a, b)

# Типа private и каждый раз словарь не создавать
calculator.__operations__ = {
    '+' :   lambda x, y: x + y,
    '-' :   lambda x, y: x - y,
    '*' :   lambda x, y: x * y,
    '/' :   lambda x, y: x / y,
    '//':   lambda x, y: x // y,
    '%' :   lambda x, y: x % y,
    '**':   lambda x, y: x ** y
}

if __name__ == '__main__':

    a = inputNum()
    b = inputNum()
    operation = input('Введите оператор: ')

    print('{} {} {} = {}'.format(
        a, operation, b, 
        calculator(a, b, operation)
    ))