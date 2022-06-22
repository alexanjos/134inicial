# Configura
# Bibliotecas / Imports
from selenium import webdriver



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

    # Fim
    def teardown_method(self):
        # destruir o oobjeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    def testar_comprar_passagem(self):
        # e2e / end to end / ponta a ponta
        # Página Inicial (Home)
        # Executa / Valida

        # Página Lista de Passagens
        # Executa / Valida

        # Página de Compra
        # Executa / Valida

        # Página de Obrigado
        # Executa / Valida

    # Valida