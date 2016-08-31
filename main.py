from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time

#Datos personales cuenta HTCMania
htcmania_username = "<TU_USUARIO_DE_HTCMANIA>"
htcmania_password = "<TU_PASSWORD>"
htcmania_userid = "<TU_ID_DE_USUARIO>"

#Lista de enlaces donde tienes tus posts de venta
up_links = []

#Lista de mensajes a postear. Personalizar para menos sospechas!
up_strings = [
    'Arriba!',
    'Vamos, una subidita!',
    'Venga, vamos!',
    'Up!',
    'Pa arriba!',
    'Seguimos!',
    'Que me lo quitan de las manos!'
]

browser = webdriver.Firefox()
browser.get('http://htcmania.com')

try:
    name = browser.find_element_by_xpath('//a[@href="http://www.htcmania.com/member.php?u=%s"]' % htcmania_userid)
    assert name.text == htcmania_username
except:
    #Tenemos que hacer login!
    username = browser.find_element_by_id('navbar_username')
    username.send_keys(htcmania_username)

    password = browser.find_element_by_id('navbar_password')
    password.send_keys(htcmania_password)

    btn = browser.find_element_by_xpath('//input[@type="submit" and @value="Acceder al foro"]')
    btn.click()

    time.sleep(5)

for link in up_links:
    browser.get(link)

    #Buscamos el textarea donde poner el mensaje de respuesta y ponemos uno aleatorio de la lista
    textbox = browser.find_element_by_xpath('//textarea[@name="message"]')
    textbox.send_keys(up_strings[randint(0,len(up_strings)-1)])

    #Enviamos el mensaje
    send_btn = browser.find_element_by_xpath('//input[@type="submit" and @id="qr_submit"]')
    send_btn.click()

    #Esperamos 35 o mas (menos de 3 minutos) segundos entre mensaje y mensaje (limite del foro y seguridad anti bots)
    time.sleep(randint(35,180))

