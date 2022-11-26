from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton as IKB, Message
from pydrive2.drive import GoogleDrive
from ...configs.texts import NO_FILES


async def list_drive(drive: GoogleDrive, msg: Message):

    
    params = {
        "q" : "'root' in parents and trashed=false",
        "corpora":"teamDrive",
        "teamDriveId":"0AN5Lkp8pZu3HUk9PVA",
        "includeTeamDriveItems":"true",
        "supportsTeamDrives":"true"
        }
    
    buttons = []

    listed_files = drive.ListFile(params).GetList()
    
    for files in listed_files:

        buttons.append(
            [
                IKB(text=f"📄{files['title']}", 
                    url=f"{files['alternateLink']}",
                    )
            ]
        )
    
    if buttons == []:
        await msg.edit(NO_FILES)
    else:
        listed = InlineKeyboardMarkup(buttons)

        await msg.edit("Aqui tiene sus archivos", reply_markup=listed)