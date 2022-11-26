from pydrive2.drive import GoogleDrive
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton as IKB, CallbackQuery 
from ...configs.texts import FILE_UPLOADED

import json

def read_json():
    with open("config.json", "r") as file:
        data = json.load(file)
        file.seek(0)
    return data

async def upload(drive: GoogleDrive, filename, msg: Message = None, length = None):
    
    metadata = {
        'title': filename
    }

    file = drive.CreateFile(metadata)

    message = await msg.reply("Subiendo {}".format(file['title']))
    
    file.SetContentFile(file['title'])
    file.Upload()

    await message.delete()
    
    await msg.reply(FILE_UPLOADED.format(filename, length, file['id']), 
    reply_markup=InlineKeyboardMarkup(
        [
            [
                IKB("Link al archivo🔗", url=file['alternateLink']),
                
                IKB("Eliminar archivo♻️", callback_data='call_del')
            ]
        ]
        ))
    return file

async def upload_to_tdd(drive: GoogleDrive, filename, msg: Message = None, length = None):
    
    data = read_json()

    metadata = {
    'title': filename,
    'parents': [{
        'teamDriveId': data['SD_id'],
        'id': data['folder_id']
    }]
    }

    tdd_file = drive.CreateFile(metadata)

    message = await msg.reply("Subiendo {}".format(tdd_file['title']))
    
    tdd_file.SetContentFile(tdd_file['title'])
    tdd_file.Upload()

    await message.delete()
    await msg.reply(FILE_UPLOADED.format(filename, length, tdd_file['id']), 
    reply_markup=InlineKeyboardMarkup(
        [
            [
                IKB("Link al archivo🔗", url=tdd_file['alternateLink']),
                
                IKB("Eliminar archivo♻️", callback_data='call_del')
            ]
        ]
        ))
    return tdd_file

