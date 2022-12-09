Antes de todo debe activar la API de Drive con un correo, luego descargar el json con los detalles de drive, al bajarlo renombrarlo como client_secrets.json y luego 
ejecutar login.py para crear el credentials_module.json (Si usted ya tiene creado el credentials_module.json, ahorrese todo esto)


Para activar la API de Drive debe hacer lo siguiente:

1 - Ir a https://console.cloud.google.com/ (Con VPN obviamente)
2 -  Seleccionar un proyecto (Crear uno si no tiene ninguno)
3 - En la barra lateral de la izquierda, expanda API y autenticación y seleccione API.
4 - En la lista que se muestra de las API disponibles, haga clic en el enlace API de Drive y haga clic en Habilitar API.
5 - Hacer todo lo que sale en las fotos de https://telegra.ph/Pasos-para-crear-client-secretsjson-12-09 para crear client_secrets.json
6 - Ejecutar login.py


Una vez hecho todo esto, abrir el config.json y en SD_id, poner el ID de su Shared Drive, en caso de que vaya a subir a ahi, y si rellena esa, rellenar tambien el 
folder_id con el id de la carpeta a donde subira el bot en el Shared Drive, para cambiar entre el Shared Drive y el Personal Drive use el comando /drive

Vaya a src/configs/bot_cfgs.py y agregue todas las credenciales para el uso del bot

Lista de comandos:

```
/start - Inicia el bot
/help - Muestra mensaje de ayuda
/drive - Seleccionar tipo de drive
/list - lista las cosas solo de su nube personal
/del {link} - elimina el archivo de su drive, asegurese de que es un archivo que esta en su drive
/count {link} - saca informacion de cualquier archivo aunque no este en su drive
```

Soporte de Sitios:
- Google Drive
- Links directos
- Mediafire
- ZippyShare
