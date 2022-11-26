import json

from pyrogram.types import (
    Message, 
    InlineKeyboardMarkup as IKM, 
    InlineKeyboardButton as IKB
)



def read_json():
    with open("config.json", "r") as file:
        data = json.load(file)
        file.seek(0)
    return data


async def open_json(selection, info_data: str = None):
    
    with open("config.json", "r+") as file:
            data = json.load(file)
            data[info_data] = bool(selection)
            file.seek(0)
            file.write(json.dumps(data, indent=4))
            file.truncate()


async def select_drive(msg: Message):

    await msg.reply(
        "Seleccione a donde desea subir⬆️",
        reply_markup=IKM(
            [
                [
                    IKB("Personal👤", callback_data='personal'),
                    IKB("TeamDrive👥", callback_data='td')
                ]
            ]
        )
    )