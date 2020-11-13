from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import bs4
import selenium

#navegar até o whatsapp
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)
#definir contatos ou grupos
contatos = ['Anotações']
mensagem = 'salve pai'
arquivo = ''
#buscando os grupos
def buscar_contato(contato):
    campop_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campop_pesquisa.click()
    campop_pesquisa.send_keys(contato)
    campop_pesquisa.send_keys(Keys.ENTER)
    time.sleep(5)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
        
    

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)


#campo de pesquisa copyable-text selectable-text
#campo mensagem privada copyable-text selectable-text


