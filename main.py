def print_hi(name):
    print(f'Hi, {name}')


def somar(number_a, number_b):
    return number_a + number_b
    # result = number_a + number_b
    # return result


def dividir(number_a, number_b):
    try:
        return number_a / number_b
    except ZeroDivisionError:
        return 'Não dividiras por zero'


def subtrair(number_a, number_b):
    return number_a - number_b


def multiplicar(number_a, number_b):
    return number_a * number_b


if __name__ == '__main__':
    print_hi('World')

    result = somar(5, 7)
    print(f'O resultado da soma é {result}')

    # Teste Git
