from pyrogram import Client as app,filters
from kvsqlite.sync import Client as q

db = q("data.sqlite",'users')
@app.on_message(filters.private & filters.command(['start']) , group=1)
def r(app,msg):
    if db.exists(f"user_{msg.from_user.id}"):
        
        msg.reply("اهلاً،\n[ شرح للبوت ]:\nمن خلال أرسالك لملف ميديا او ملف عادي سوف يتم رفعهُ وحفظه. ويمكنك إسترداده بأي وقت تُريد.\n[ الاوامر ]:\nلرؤية اوامر البوت أرسل: /help\n.")
    else:
        db.set(f'user_{msg.from_user.id}',{'data':[]})
        msg.reply("اهلاً،\n[ شرح للبوت ]:\nمن خلال أرسالك لملف ميديا او ملف عادي سوف يتم رفعهُ وحفظه. ويمكنك إسترداده بأي وقت تُريد.\n[ الاوامر ]:\nلرؤية اوامر البوت أرسل: /help\n.")
@app.on_message(filters.private & filters.command(['help']), group=2)
def r2(app, msg):
    msg.reply("[ قائمة الاوامر ]:\n1. /list - يقوم بجلب جميع الملفات التي قمت برفعها مسبقاً .\n2. /get fileid - يقوم بجلب ملف معين من الخزن بأستخدام ايدي الملف .\n.")
    