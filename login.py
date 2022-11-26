from pydrive2.auth import GoogleAuth

"""

Antes de todo debe activar la API de Drive con un
correo, descargar el json con los detalles de drive,
al bajarlo renombrarlo como client_secrets.json
(Dejare unas fotos de todas maneras)
y luego ejecutar este script,  para activar
la API de Drive debe hacer lo siguiente:

1 - Ir a https://console.cloud.google.com/ (Con VPN obviamente)
2 -  Seleccionar un proyecto (Crear uno si no tiene ninguno)
3 - En la barra lateral de la izquierda, expanda API y autenticación 
    y seleccione API.
4 - En la lista que se muestra de las API disponibles, haga clic en 
    el enlace API de Drive y haga clic en Habilitar API.

"""

def login():
    gauth = GoogleAuth(settings_file='./src/configs/conf.yaml')
    gauth.LocalWebserverAuth(launch_browser=True)


login()