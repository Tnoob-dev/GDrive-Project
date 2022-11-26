from pydrive2.drive import GoogleDrive
from pyrogram.emoji import BACKHAND_INDEX_POINTING_DOWN, CROSS_MARK
from pyrogram.types import Message, CallbackQuery



async def delete(msg: Message, drive: GoogleDrive):
    
    try:
        # message = await msg.reply(f"Eliminando {CROSS_MARK}{file1['title']}{CROSS_MARK}...")
        file1 = drive.CreateFile({'id': msg.text.split(" ")[1].split("/")[-2]})
        file1.Upload()
        file1.Delete()
        await msg.reply(f"Se ha borrado correctamente {file1['title']}😋")
    except Exception as e:
        print(e)
        await msg.reply(f"❌Error al borrar: {BACKHAND_INDEX_POINTING_DOWN}\n\n{e}")

async def query_delete(query: CallbackQuery,drive: GoogleDrive, file):
    
    try:
        # message = await query.message.reply(f"Eliminando {CROSS_MARK}{file['title']}{CROSS_MARK}...")
        file = drive.CreateFile({'id': file['id']})
        file.Upload()
        file.Delete()
        await query.message.edit(f"Se ha borrado correctamente {file['title']}😋")
    except Exception as e:
        print(e)
        await query.message.reply(f"❌Error al borrar: {BACKHAND_INDEX_POINTING_DOWN}\n\n{e}")