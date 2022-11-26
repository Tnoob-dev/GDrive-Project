import os
from pathlib import Path

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive



gauth = GoogleAuth(settings_file='./src/configs/conf.yaml')
gauth.LoadCredentialsFile("credentials_module.json")

if gauth.access_token_expired:
    gauth.Refresh()
    gauth.SaveCredentialsFile("credentials_module.json")
else:
    gauth.Authorize()

# gauth.LocalWebserverAuth(launch_browser=False)
drive = GoogleDrive(gauth)

from logging import log, basicConfig, getLogger, INFO, ERROR, WARN

basicConfig(level=INFO, force=True, format="[%(levelname)s - %(asctime)s - %(message)s]")

drive_bot = getLogger("pyroDrive")
drive_bot.setLevel(WARN)

log(INFO, "Iniciando Logger")

from pyrogram import Client, filters
from pyrogram.types import (
    Message, 
    InlineKeyboardButton as IKB, 
    InlineKeyboardMarkup as IKM, 
    CallbackQuery
)

# mis modulos
from src.configs.bot_cfgs import (
    SESSION, 
    BOT_TK, 
    HASH, 
    ID, 
    OWNER
)

from src.configs.texts import (
    START_MESSAGE, 
    GENERAL_HELP_MESSAGE, 
    COMMANDS_HELP_MESSAGE,
    SUPPORT_DLS_MESSAGE,
    NO_AUTH,
    ERROR_IN_TRY
    )




from src.plugins.drive_modules.list_drive import list_drive
from src.plugins.drive_modules.delete import delete, query_delete
from src.plugins.drive_modules.count import drive_count
from src.plugins.drive_modules.json_file import open_json, read_json, select_drive
from src.plugins.drive_modules.upload import upload, upload_to_tdd

from src.plugins.downloads.reqs import aiodl
from src.plugins.downloads.mf_dl import download
from src.plugins.downloads.zippy import zdl
from src.plugins.downloads.drive_dl import gdl




bot: Client = Client(
    name=SESSION,
    api_hash=HASH,
    api_id=ID,
    bot_token=BOT_TK
)


@bot.on_message(filters.command("start", prefixes="/"))
async def start(client: Client, message: Message):

    if message.from_user.id == OWNER:

        await message.reply(START_MESSAGE.format(
    message.from_user.mention
    ),
    reply_markup=IKM(
        [
            [
                IKB("Ayuda🛐", callback_data='help')
            ]
        ]
    ))
    else:
        await message.reply(NO_AUTH)

@bot.on_message(filters.command("help", prefixes="/"))
async def help(client: Client, message: Message):
    
    if message.from_user.id == OWNER:
        await message.reply(GENERAL_HELP_MESSAGE.format(
            message.from_user.mention
        ), reply_markup=IKM(
                [
                    [
                        IKB("💬Comandos", callback_data='commands'),
                        IKB("⬇️Soporte de descarga", callback_data='supp_down')
                    ]
                ]
            ))
    else:
        await message.reply(NO_AUTH)

@bot.on_message(filters.command("drive", prefixes="/"))
async def drive_selection(client: Client, message: Message):
    
    if message.from_user.id == OWNER:
        await select_drive(message)
    else:
        await message.reply(NO_AUTH)


@bot.on_message(filters.command("list", prefixes="/"))
async def list_files_drive(client: Client, message: Message):
    
    if message.from_user.id == OWNER:

        msg = await message.reply("Listando archivos")
        await list_drive(drive, msg)
    
    else:
        await message.reply(NO_AUTH)

@bot.on_message(filters.command("del", prefixes="/"))
async def del_files(client: Client, message: Message):
    
    if message.from_user.id == OWNER:
        await delete(message, drive)
    else:
        await message.reply(NO_AUTH)


@bot.on_message(filters.command("count", prefixes="/"))
async def count(client: Client, message: Message):

    if message.from_user.id == OWNER:

        await drive_count(message, drive)
    
    else:
        await message.reply(NO_AUTH)

@bot.on_message(filters.regex(".*https://.*") | filters.regex(".*http://.*"))
async def dls(client: Client, message: Message):

    if message.from_user.id == OWNER:

        data = read_json()

        global file
        global tdd_file

        if 'mediafire' in message.text:
            log(INFO, "Link de mediafire detectado!")
            output, total_length, msg = await download(message.text, message.text.split("/")[-2], quiet=False, message=message)
            
            try:

                if data['teamDrive'] is False:
                    await msg.delete()
                    file = await upload(drive, output, message, total_length)
                elif data['teamDrive'] is True:
                    await msg.delete()
                    tdd_file = await upload_to_tdd(drive, output, message, total_length)

            except Exception as e:
                log(INFO, e)
                await message.reply(ERROR_IN_TRY)
                
        elif 'zippyshare' in message.text:
            log(INFO, "Link de zippyshare detectado!")
            Zfile, msg = await zdl(message.text, message)
            try:
                if data['teamDrive'] is False:
                    await msg.delete()
                    file = await upload(drive, Zfile.name, message, Zfile.size_fmt)
                elif data['teamDrive'] is True:
                    await msg.delete()
                    tdd_file = await upload_to_tdd(drive, Zfile.name, message, Zfile.size_fmt)

            except Exception as e:
               log(INFO, e)
               await message.reply(ERROR_IN_TRY)

        elif 'drive' in message.text:
            log(INFO, "Link de drive detectado!")
            Gfile, msg = await gdl(drive, message.text, message)

            try:
                if data['teamDrive'] is False:
                    await msg.delete()
                    file = await upload(drive, Gfile['title'], message, Path(Gfile['title']).stat().st_size / 1000000)
                elif data['teamDrive'] is True:
                    await msg.delete()
                    file = await upload_to_tdd(drive, Gfile['title'], message,Path(Gfile['title']).stat().st_size / 1000000)
            except Exception as e:
               await message.reply(e)
               log(INFO, e)
               await message.reply(ERROR_IN_TRY)

        else:
            log(INFO, "Link directo detectado!")
            filename, final_length, msg = await aiodl(message.text, message)
            
            try:
                if data['teamDrive'] is False:
                    await msg.delete()
                    file = await upload(drive, filename, message, final_length)
                elif data['teamDrive'] is True:
                    await msg.delete()
                    tdd_file = await upload_to_tdd(drive, filename, message, final_length)
            except Exception as e:
               log(INFO, e)
               await message.reply(ERROR_IN_TRY)

    else:
        await message.reply(NO_AUTH)

@bot.on_callback_query()
async def del_f(client: Client, query: CallbackQuery):
    
    back = [IKB("⬅️Regresar", callback_data='help')]
    close = [IKB("❌Cerrar", callback_data='close')]
    data = read_json()

    if query.data == 'call_del':

        await query.answer('Eliminando')

        if data['teamDrive'] is False:
            await query_delete(query=query, drive=drive, file=file)
        
        elif data['teamDrive'] is True:
            await query_delete(query=query, drive=drive, file=tdd_file)
    
    elif query.data == 'help':

        await query.message.edit(
            GENERAL_HELP_MESSAGE,
            reply_markup=IKM(
                [
                    [
                        IKB("💬Comandos", callback_data='commands'),
                        IKB("⬇️Soporte de descarga", callback_data='supp_down')
                    ]
                ]
            )
            )

    elif query.data == 'commands':

        await query.message.edit(
            COMMANDS_HELP_MESSAGE, 
            reply_markup=IKM(
                [
                    back,
                    close
                ]
            )
            )

    elif query.data == 'supp_down':
        await query.message.edit(
            SUPPORT_DLS_MESSAGE,
            reply_markup=IKM(
                [
                    back,
                    close
                ]
            ),
            disable_web_page_preview=True
            )
    elif query.data == 'personal':

        await open_json(False, 'teamDrive')
        await query.message.edit("Vale, subiremos a su nube personal")
    
    elif query.data == 'td':

        await open_json(True, 'teamDrive')
        await query.message.edit("Vale, subiremos a su TeamDrive")

    elif query.data == 'close':
        await query.message.delete()

if __name__ == "__main__":
    log(INFO, "Iniciando el Bot")
    bot.start()
    log(INFO, "Bot iniciado")
    bot.loop.run_forever()