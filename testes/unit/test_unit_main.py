from main import somar, dividir, multiplicar, subtrair


def tester_somar():
    # 1 - Configura
    number_a = 5
    number_b = 7
    result_esperado = 12

    # 2 - Executa
    result_obtido = somar(number_a, number_b)

    # 3 - Valida
    assert result_esperado == result_obtido


def teste_dividir_positivo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    number_a = 50
    number_b = 5

    # 1.2 - Resultados Esperados
    result_esperado = 10

    # 2 - Executa
    resultado_obtido = dividir(number_a, number_b)

    assert result_esperado == resultado_obtido


def teste_dividir_negativo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    number_a = 50
    number_b = 0

    # 1.2 - Resultados Esperados
    result_esperado = 'Não dividiras por zero'

    # 2 - Executa
    resultado_obtido = dividir(number_a, number_b)

    assert result_esperado == resultado_obtido


def teste_multiplicar():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    number_a = 10
    number_b = 5

    # 1.2 - Resultados Esperados
    result_esperado = 50

    # 2 - Executa
    resultado_obtido = multiplicar(number_a, number_b)

    assert result_esperado == resultado_obtido


def teste_subtrair():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    number_a = 20
    number_b = 12

    # 1.2 - Resultados Esperados
    result_esperado = 8

    # 2 - Executa
    resultado_obtido = subtrair(number_a, number_b)

    # Valida
    assert result_esperado == resultado_obtido
