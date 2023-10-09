from pyrogram import Client,filters
import pyrogram
plugins = dict(root="plugins")

Client("boty",15102119,'3dfdcee3e3bedad4738f81287268180f',bot_token='Token', plugins=plugins, parse_mode=pyrogram.enums.ParseMode.HTML).run()