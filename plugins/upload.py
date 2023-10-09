from pyrogram import Client as app,filters
import requests,re,shutil
from kvsqlite.sync import Client as q
db = q("data.sqlite",'users')

def upload(file_path: str) ->str:
    response = requests.post("https://api.anonfiles.com/upload",files={'file':open(file_path,"rb")})
    url = (response.json()["data"]["file"]["url"]["short"])
    txt = requests.get(url).text
    find_link = re.findall('href="(.*?)">',txt)[3]
    return {"link":find_link , "id": url.split("/")[-1]}
@app.on_message(filters.media  & filters.document & filters.private, group=3)
def g(app, msg):
    if msg.photo:
        file_type = 'صورة'
        file_id = msg.photo.file_id
        file_name = f"image.jpg"
        size = msg.photo.file_size
    elif msg.audio:
        file_type = 'صوتية'
        file_id = msg.audio.file_id
        file_name = str(msg.audio.file_name).replace(' ','')
        size = msg.audio.file_size
    elif msg.voice:
        file_type = 'فويس'
        file_id = msg.voice.file_id
        file_name = f"u.ogg"
        size = msg.voice.file_size
    elif msg.video:
        file_type = 'فيديو'
        file_id = msg.video.file_id
        file_name = str(msg.video.file_name).replace(' ','')
        duration = msg.video.duration
        size = msg.video.file_size
    elif msg.document:
        file_type = 'ملف'
        file_name = msg.document.file_name
        size = msg.document.file_size
    else:
        # Handle unsupported file types here
        return
    
    if file_type:
        msg.download(f"temp/{file_name}")
        z = msg.reply('[ جاري رفع الملف  ] ..')
        link = upload(f'temp/{file_name}')
        d = {"id":link['id'], "url": link['link'], 'media': file_type, 'filename': file_name, 'size':size}
        if file_type == 'video':
            d['duration'] = duration
        x_ = db.get(f"user_{msg.from_user.id}")
        x_['data'].append(d)
        db.set(f'user_{msg.from_user.id}', x_)
        app.delete_messages(msg.chat.id,z.id )
        msg.reply(f"[ عملية رفع ناجحة ]\nالملف: {file_name}، \nحجمه: {size}،\nنوعه: {file_type}،\nايدي: {link['id']}")
        import os
        folder = "temp"
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            os.remove(file_path)