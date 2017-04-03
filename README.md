# HTCMania Poster

Esto es un script para postear automaticamente en el foro de venta de HTCMania. 

> NOTA IMPORTANTE: Este Script se ha creado con el proposito de evitar tener que postear cada dia un "up!" en el post de venta para tener que subir nuestro post. Solo tiene este proposito y no hace nada que perjudique a la web. Es simplemente una herramienta para facilitar vender las cosas en el foro a los que no tienen tiempo de estar cada dia enviando mensajes. Fuera de esto, si se usa para acciones mal intencionadas queda fuera de mi responsabilidad. 

## Requisitos

1. Tener Firefox instalado y listo para ejecutar.
2. Instalar Python 2.7 e incluir en la ruta del PATH.
3. Instalar Selenium (WebDriver para usar automaticamente un Navegador) ```pip install -U selenium```

## Uso

* Editamos el fichero 'main.py' la primera parte. Debemos introducir nuestros datos:

```
#Datos personales cuenta HTCMania
htcmania_username = "<TU_USUARIO_DE_HTCMANIA>"
htcmania_password = "<TU_PASSWORD>"
htcmania_userid = "<TU_ID_DE_USUARIO>"
```
El ID de Usuario lo encontramos entrando en nuestro perfil y copiando el numero del final de la URL. Ejemplo:

'http://www.htcmania.com/member.php?u=1' donde 1 es el ID de usuario.

* Editamos la lista de URL's donde tenemos nuestros post de venta.
```
#Lista de enlaces donde tienes tus posts de venta
up_links = [
    'http://www.htcmania.com/showthread.php?t=...',
    '...'
]
```
* Editamos la lista de palabras de subida (para que cante menos la automatización)
```
up_strings = [
    'Arriba!',
    'Vamos, una subidita!',
    'Venga, vamos!',
    'Up!',
    'Pa arriba!',
    'Seguimos!',
    'Que me lo quitan de las manos!'
]
```
* Damos permisos de ejecución (Linux): ```chmod u+x main.py```
* Ejecutamos y a ver la magia!  ```python main.py```
