# Configura
# Bibliotecas / Imports
import time

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


# Dados de Entrada


origem = 'São Paolo'
destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
titulo_passagens_esperados = 'Flights from São Paolo to New York:'
mensagem_de_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'


# Executa
class Testes:

    # Início
    def setup_method(self):
        # instanciar a biblioteca / motor / engine
        # informar onde está o WebDriver
        self.driver = webdriver.Chrome()
        # Espera até 15 segundos por qualquer elemento
        self.driver.implicitly_wait(15)

    # Fim
    def teardown_method(self):
        # destruir o oobjeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    def testar_comprar_passagem(self):
        # e2e / end to end / ponta a ponta
        # Página Inicial (Home)
        # Executa / Valida
        # Abrir o browser no endereço
        self.driver.get('https://www.blazedemo.com')
        lista = self.driver.find_element(By.NAME, "fromPort")
        lista.click()
        # selecionar a cidade de origem
        lista.find_element(By.XPATH, f'//option[ .= "{origem}"]').click()
        # clicar na lista de cidades de destino
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()
        # Selecionar a cidade de destino na lista
        lista.find_element(By.XPATH, f'//option[ .= "{destino}"]').click()
        # Clicar no botão de procurar voos
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()


        # Página Lista de Passagens
        # Executa / Valida
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == titulo_passagens_esperados
        self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) .btn').click()
        time.sleep(2)

        # Página de Compra
        # Executa / Valida

        # Página de Obrigado
        # Executa / Valida

    # Valida