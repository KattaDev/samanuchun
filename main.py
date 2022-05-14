
import logging
import sqlite3
import json
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1651301432:AAGcjEGXIcSN0Lhq-DDshgsMdjonAxbbWvM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# create a database connection
conn=sqlite3.connect("worddata.db")
# create a cursor
cur = conn.cursor()
emojlisti=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
def get_word(word):
        mean=word[0][1]
        mean=mean.replace("'","\"")
        jsonmean=json.loads(mean)
        javob=''
        for i in jsonmean:
            soni=0
            for j in i["meanings"]:
              
                javob=javob+'<b>{} '.format(emojlisti[soni])+j["text"]+"</b>\n"
                soni+=1
        return javob

def getizoh(word):
    word = word.lower()
    word = word.replace("ʻ", "ʻ")
    word=word.replace("'","ʻ")
    word1=word.upper()
    javob="<b>{} so'zinig izohi.</b>\n\n".format(word1)
    cur.execute("SELECT * FROM izohlar WHERE word = ?", (word,))
    rows = cur.fetchall()
    print(rows)
    if len(rows) == 0 or rows[0][1]=="None" or len(rows[0][1])==0:
        word=word.replace("ʻ","ʼ")
        cur.execute("SELECT * FROM izohlar WHERE word = ?", (word,))
        rows = cur.fetchall()
        print(rows)
        if len(rows) == 0 or rows[0][1]=="None"or len(rows[0][1])==0:
            
            return "<b>Bunday so'z topilmadi.\n So'z to'g'ri yozilganligiga e'tibor bering!</b>"
        else:
            return javob+get_word(rows)
    else:
        return javob+get_word(rows)

@dp.message_handler()
async def echo(message: types.Message):
    javobi=getizoh(message.text)
    await message.answer(javobi,
                        parse_mode=types.ParseMode.HTML)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
