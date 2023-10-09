from pyrogram import Client as app,filters
import requests,re,shutil
from kvsqlite.sync import Client as q
db = q("data.sqlite",'users')
def getl(id):
    
    url = f"https://anonfiles.com/{id}"
    txt = requests.get(url).text
    find_link = re.findall('href="(.*?)">',txt)[3]
    return find_link
@app.on_message(filters.private & filters.command(['list']), group=4)
def gt(app,msg):
    x = "[ قائمه الملفات ]:\n"
    z = db.get(f"user_{msg.from_user.id}")
    if len(z['data']) <1:
        return msg.reply("[ لم يتم العثور على اي ملف ] .")
    else:
        for i in z['data']:
            x+=f"""
- id: {i['id']} 
 ├ Type: {i['media']}
 ├ name: {i['filename']}
 └ Size: {i['size']}
 
            """
        x+="[ للحصول او تحميل ملف معين ارسل ]:\n/get id ."
        msg.reply(x)
@app.on_message(filters.private & filters.regex(r"^/get (.*?)"), group=5)
def getf(app , msg):
    id = msg.text.split("/get ")[1]
    fi = None
    info = db.get(f'user_{msg.from_user.id}')
    for i in info['data']:
        if i['id'] == id:
            fi = i
        else:
            continue
    if fi != None:
        file_name = fi['filename']
        link = getl(id)
        try:
            from pySmartDL import SmartDL
    
            url = link
            path = f"temp/{file_name}"
            
            obj = SmartDL(url, dest=path, progress_bar=False)
            obj.start()
            if obj.isSuccessful():
                path = obj.get_dest()
                msg.reply_document(path)
            else:
                msg.reply(f"Failed to download file")
        except:
            pass