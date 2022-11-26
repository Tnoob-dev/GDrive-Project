from pyrogram.types import Message
from pyrogram.emoji import BACKHAND_INDEX_POINTING_DOWN, MAGNIFYING_GLASS_TILTED_LEFT
from pydrive2.drive import GoogleDrive
from ...configs.texts import RESULT_IN_COUNT

async def drive_count(msg: Message, drive: GoogleDrive):
    
    try:
        message = await msg.reply(f"Buscando archivo {MAGNIFYING_GLASS_TILTED_LEFT}...")
        file = drive.CreateFile({'id': msg.text.split(' ')[1].split('/')[-2]})
        file.FetchMetadata()
        
        result = RESULT_IN_COUNT.format(
            
            file['title'], 
            int(file['fileSize']) / 1000000, 
            file['fileExtension'], 
            file['mimeType'])

        await message.edit(result)
    except Exception as e:
        await msg.reply(f"Error en el comando /count: {BACKHAND_INDEX_POINTING_DOWN}\n\n{e}")