from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

# Especifique o caminho para o ChromeDriver
chrome_driver_path = "/Users/jorgejaujr/Desktop/virtualenv/testes/chromedriver"  # Altere para o caminho correto

# Configurar o serviço e opções do Chrome
service = Service(chrome_driver_path)
options = Options()

# Iniciar o WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Acessar a URL desejada
url = "https://veiculos.fipe.org.br/"
driver.get(url)

listaData = []
listaMarcaCarro = []
listaAnoModeloCarro = []
listaAnoCarro = []
listaFinal = []

driver.find_element(By.XPATH, "//a[@data-action='veiculos']").click()
time.sleep(1)

#Clica para abrir a lista de montadoras e gerar a lista de modelos daquela montadora
driver.find_element(By.XPATH, "//div[@id='selectTabelaReferenciacarro_chosen']//a").click()

opcoesData = Select(driver.find_element(By.ID, "selectTabelaReferenciacarro")).options
for element in opcoesData:
    listaData.append(element.get_attribute("innerText"))
driver.find_element(By.XPATH, "//div[@id='selectTabelaReferenciacarro_chosen']//div[@class='chosen-drop']//ul//li[@data-option-array-index='2']").click()

driver.find_element(By.XPATH, "//div[@id='selectMarcacarro_chosen']").click()

opcoesMarca = Select(driver.find_element(By.ID, "selectMarcacarro")).options
for element in opcoesMarca:
    listaMarcaCarro.append(element.get_attribute("innerText"))
driver.find_element(By.XPATH, "//div[@id='selectMarcacarro_chosen']//div[@class='chosen-drop']//div//input").send_keys(f'{listaMarcaCarro[1]}\n')

opcoesModelo = Select(driver.find_element(By.ID, "selectAnoModelocarro")).options
for element in opcoesModelo:
    listaAnoModeloCarro.append(element.get_attribute("innerText"))

driver.find_element(By.XPATH, "//div[@id='selectAnoModelocarro_chosen']").click()
driver.find_element(By.XPATH, "//div[@id='selectAnoModelocarro_chosen']//div[@class='chosen-drop']//div//input").send_keys(f'{listaAnoModeloCarro[3]}\n')

opcoesAnoModelocarro = Select(driver.find_element(By.ID, "selectAnocarro")).options
for element in opcoesAnoModelocarro:
    listaAnoCarro.append(element.get_attribute("innerText"))


driver.find_element(By.XPATH, "//div[@id='selectAnocarro_chosen']").click()
driver.find_element(By.XPATH, "//div[@id='selectAnocarro_chosen']//div[@class='chosen-drop']//div//input").send_keys(f'{listaAnoCarro[1]}\n')


driver.find_element(By.XPATH, "//a[@id='buttonPesquisarcarro']").click()

tbl = driver.find_element(By.XPATH, "//table").get_attribute('outerHTML')
tabela = pd.read_html(tbl,index_col=0)
listaFinal.append(tabela[0])
print(listaFinal)

time.sleep(5)

driver.close()