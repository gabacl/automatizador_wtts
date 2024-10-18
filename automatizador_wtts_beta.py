#Automatizador beta

#abrir o whatsapp, selecionar a barra de pesquisa, achar o contato desejado, clicar no contato, localizar a barra de texto e clicar nela, colar o texto, localizar e clicar no botão de enviar.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico=Service(ChromeDriverManager().install())

driver=webdriver.Chrome(service=servico)

driver.get('https://web.whatsapp.com/')
time.sleep(15)

driver.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys('Eu')
time.sleep(3)
driver.find_element('xpath', '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]').click()
time.sleep(3)
driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p').send_keys('teste 1')
time.sleep(1)
driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button/span').click()
time.sleep(5)

driver.quit()

#usar time sleep foi no momento a unica solução que encontrei pro navegador não fechar no momento em que logar o wtts
