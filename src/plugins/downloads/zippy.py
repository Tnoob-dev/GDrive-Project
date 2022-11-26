from zippyshare_downloader import extract_info_coro
from pyrogram.types import Message
async def zdl(url: str, message: Message):

    msg = await message.reply("Descargando")

    Zfile = await extract_info_coro(url, download=True)
    
    return Zfile, msg