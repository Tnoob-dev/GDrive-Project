import aiohttp
from yarl import URL
from pyrogram.types import Message

async def aiodl(url: str, message: Message):
    # Se puede usar este:
    # filename = url.split('/')[-1]
    # o este:
    msg = await message.reply("Descargando")
    filename = URL(url).name # Recomendado
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=None) as response:
            length = int(response.headers.get('content-length'))
            with open(filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
                    f.flush()
                    print('\r{:.2f}%'.format(f.tell() * 100 / length), end='')
            final_length = f'{length / 1000000:.2f}'
            
    return filename, final_length, msg