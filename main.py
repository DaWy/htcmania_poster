#!/usr/bin/python2.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from spin import SpinCursor
import time
import selenium
from pyvirtualdisplay import Display



#Datos personales cuenta HTCMania
htcmania_username = ""
htcmania_password = ""
htcmania_userid = ""

#Lista de enlaces donde tienes tus posts de venta
up_links = [
    'https://www.htcmania.com/showthread.php?p=31113029'
    #'http://www.htcmania.com/showthread.php?t=1254708', #Surface Pro 3
    #'http://www.htcmania.com/showthread.php?t=1287144', #Zuk Z2
]

#Lista de mensajes a postear. Personalizar para menos sospechas!
up_strings = [
    'Seguimos!',
    'Up!!',
]

print 'Abriendo navegador...'

display = Display(visible=0, size=(1280, 800))
display.start()

browser = webdriver.Chrome()

print 'Cargando HTCMania...'

browser.get('https://htcmania.com')

try:
    name = browser.find_element_by_xpath('//a[@href="https://www.htcmania.com/member.php?u=%s"]' % htcmania_userid)
    assert name.text == htcmania_username
except:
    #Tenemos que hacer login!
    print 'Logeando usando credenciales: %s/%s' % (htcmania_username,htcmania_password)
    username = browser.find_element_by_id('navbar_username')
    username.send_keys(htcmania_username)

    password = browser.find_element_by_id('navbar_password')
    password.send_keys(htcmania_password)

    btn = browser.find_element_by_xpath('//input[@type="submit" and @value="Acceder "]')
    btn.click()

    time.sleep(5)

    #Comprobamos que realmente se ha hecho login!
    name = browser.find_element_by_xpath('//a[@href="https://www.htcmania.com/member.php?u=%s"]' % htcmania_userid)
    assert name.text == htcmania_username

for link in up_links:
    #Esperamos 35 o mas (menos de 3 minutos) segundos entre mensaje y mensaje (limite del foro y seguridad anti bots)
    waiting = randint(180,10800)
    print '\n'
    spin = SpinCursor(msg="Esperando %s segundos para el siguiente post..." % waiting, speed=5, minspin=5*waiting)
    spin.start()
    time.sleep(waiting)
    spin.stop()


    print 'Cargando: %s...' % link
    browser.get(link)
    print 'Escribiendo post y enviando!'
    #Buscamos el textarea donde poner el mensaje de respuesta y ponemos uno aleatorio de la lista
    try:
        textbox = browser.find_element_by_xpath('//textarea[@name="message"]')
        textbox.send_keys(up_strings[randint(0,len(up_strings)-1)])
        #Enviamos el mensaje
        send_btn = browser.find_element_by_xpath('//input[@type="submit" and @id="qr_submit"]')
        send_btn.click()
        print 'Post enviado!'
    except:
        print 'Error al enviar el post... => %s' % link

    

print '\n Finalizado! :)'

