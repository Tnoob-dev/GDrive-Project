from pydrive2.drive import GoogleDrive
from pyrogram.types import Message


async def gdl(drive: GoogleDrive, url: str, message: Message):

    msg = await message.reply("Descargando")
    metadata = {
        'id': url.split("/")[-2]
    }

    Gfile = drive.CreateFile(metadata=metadata)
    Gfile.GetContentFile(Gfile['title'])

    return Gfile, msg

