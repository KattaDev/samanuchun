


import requests
import time
import sqlite3




# function
def main(idim,token,message):
    res= requests.post(urllink.format(token, "sendAudio"),data={'chat_id': -1001632028870, "audio":"https://t.me/musiqabazasql/{}".format(id),'caption':"{}-{}".format(message,idim)})
    error=res.json()
    if res.ok:
        data=res.json()['result']
        if("audio" in data.keys()):
            audio=data['audio']
            file_name="audio"
            file_id="file_id"
            file_size="0"
            performer="performer"
            title="title"
            message_id=str(res.json()['result']["message_id"])
            if("file_name" in audio.keys()):
                file_name=audio['file_name']
            if ("duration" in audio.keys()):
                duration=audio['duration']
            if ("performer" in audio.keys()):
                performer=audio['performer']
            if ("title" in audio.keys()):
                title=audio['title']
            if("file_id" in audio.keys()):
                file_id=audio['file_id']
            if("file_size" in audio.keys()):
                file_size=audio['file_size']
                cursor.execute("INSERT INTO musiclar VALUES (?,?,?,?,?,?,?)", (str(message_id),str(duration),str(performer),str(title),str(file_name),str(file_size),str(file_id)))
                conn.commit()
    elif("error_code" in error.keys()and error["error_code"]==429):
        print(error)
        second=error['parameters']['retry_after']
        time.sleep(second+1)
   
    












urllink="https://api.telegram.org/bot{}/{}"
tokens=["5381502463:AAGyup56SDmfV4gkGVY-s2gIEn5TkIR7LBc","5366241422:AAEitU_b8ureTNwP4SbJ8ehTa8lnm6Ovqa4","5379006146:AAG6z5_aI3mR0c0tx9TnXnQDisaJyyjqPjg","5394771135:AAFTvWxdEiKZGRTR7QbFtg4B6rXgJZFRtCw","5183278593:AAFiyaUxIXNmoX3RIr_NLhfm0VrkORm0jiU","5263618545:AAF4ysEoJtgH7YS0AAMFzMUq2oMlwnvpvqE","5329761378:AAF7_GZUatZ7-SMe1z0qUVu-j_cgJpKCaqE","5322426976:AAGIpIS5rdO0s4ADUh4O1dHeOc-SS3_UUBU","5206916749:AAHvJqVTnz6uCIS7e7zF-uLav40C0Myn5IU","5088049634:AAFKFWyfL8trfBP51vF-GFytWDxWXnqz2o8","5086197624:AAGK6fpCiE-YtKOkqoVqBp_xewujzrww35Q","1527363428:AAGOcNvxq4RqhjkcwB5ZiyeUUT0DAI8YCrw","1632050693:AAGM9HZzTOjZI9ZsGoZpsUX_VoOpbpe3L2A","1599120318:AAFpDErwzqlM5xgzqo163R4MoqOnwxGGPD8","2008898965:AAE3SADGW0yk7PeCcHyp8kexIihPfKSdDw4","5360738038:AAFXMhK59lrNnFqj_KToCXKBBbwmIQmOq1o"]
id=0

conn = sqlite3.connect('musicdata.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE musiclar
               (message_id text, duration text, performer text, title text, file_name text, file_size text, file_id text)''')

# do while True
while id<454557:
    # for range 20
    for token in tokens:
        messageid=0
        # for token tokens
        for i in range(20):
            id=id+1
            messageid=messageid+1
            main(id, token, messageid)



