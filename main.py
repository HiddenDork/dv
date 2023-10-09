from pyrogram import Client,filters
import pyrogram
plugins = dict(root="plugins")

Client("boty",15102119,'3dfdcee3e3bedad4738f81287268180f',bot_token='6644409337:AAH7wI-B2gIHZzp2AuKfpaMH7Ky6X1PkcMs', plugins=plugins, parse_mode=pyrogram.enums.ParseMode.HTML).run()
