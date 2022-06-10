# ToDo: 3 - criar uma venda de um pet para um usuário
# ToDo: 4 - consultar os dados do pet que foi vendido
import json
import os

import requests

url = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}


def teste_vender_pet():
    # Configura
    # Dados de entrada
    # Virao do arquivo pedido1.json

    # Resultados esperados
    status_code_esperado = 200
    pedido_id_esperado = 981738121
    pet_id_esperado = 1732181
    status_pedido_esperado = 'placed'

    # Executa
    caminho = os.path.abspath(__file__ + "/../../../") + os.sep + 'vendors' + os.sep + 'json' + os.sep

    resultado_obtido = requests.post(
        url=url + 'store/order',
        headers=headers,
        data=open(caminho + 'pedido1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pedido_id_esperado
    assert corpo_do_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    # Extrai
    pet_id_extraido = corpo_do_resultado_obtido.get('petId')

    # Realizar a Segunda transação

    # Configura
    # Dados de Entrada
    # Extraidos da primeira transação acima

    # Resultado Esperado
    status_code_esperado = 200
    pet_name_esperado = 'Snoopy'

    # Executa
    resultado_obtido = requests.get(
        url=url + 'pet/' + str(pet_id_extraido),
        headers=headers
    )
    # Valida
    assert resultado_obtido.status_code == 200
    print(json.dumps(corpo_do_resultado_obtido, indent=4))


    corpo_do_resultado_obtido = resultado_obtido.json()
    assert corpo_do_resultado_obtido['name'] == pet_name_esperado
