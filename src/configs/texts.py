
START_MESSAGE = """
Hola {}, 

Este bot se basa especificamente en el auxilio
al usuario a subir a su nube de Google Drive,
para ver la ayuda, donde se especificaran los
comandos, desde donde el bot soporta links de
descarga, etc..., puede usar el comando /help
o presionar en el boton que se le muestra debajo
"""

GENERAL_HELP_MESSAGE = """
Bot para mejorar la experiencia del usuario
al subir a su nube de Google Drive, seleccione 
la opcion que desea
"""

COMMANDS_HELP_MESSAGE = """
/start - Inicia el bot y muestra texto de bienvenida
/help - Muestra el Mensaje de Ayuda
/drive - Permite seleccionar a la unidad que desea subir
/list - Lista sus cosas en la nube
/count {link} - Muestra informacion acerca de el link que envie
/del {link} - Elimina el archivo del enlace que usted le envie
"""

SUPPORT_DLS_MESSAGE = """
El bot soporta enlaces de:

🔥Mediafire - Ejemplo: https://www.mediafire.com/file/e3xi44bhuqo5k4i/28_days_later.zip/file
🗂ZippyShare - Ejemplo: https://www34.zippyshare.com/v/e4i8FkKJ/file.html
🔗Links directos - Ejemplo: https://github.com/icsharpcode/ILSpy/archive/refs/tags/v7.2.1.zip
"""

LIST_FILES = "Listando archivos"

RESULT_IN_COUNT = """
ℹ️ Informacion acerca de {}: 

⚖️Tamaño: {:.2f} MB
                                               
✏️Extension: {}    
                                               
🗳Tipo: {}
"""

FILE_UPLOADED = """
Subido ✅ 

🆎Nombre: {}
⚖️Tamaño: {} MB
🆔ID: {}
"""

FILE_SELECTED = """

🆎Nombre: {}
⚖️Tamaño: {:.2f} MB
🆔ID: {}
"""


NO_FILES = "No se encontro nada en la nube😶‍🌫️"
NO_AUTH = "🚫No tiene autorizacion🚫"

ERROR_IN_TRY = "❌Ha ocurrido algun error❌"