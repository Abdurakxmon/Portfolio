import telebot
from pytube import YouTube
import glob
import requests
import os
token = '1368490503:AAGvmWgEixufaosfic5d5XN3opXlflSWqBg'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '👋 This is youtube shorts and short videoes downloader bot.')

@bot.message_handler(func=lambda message: True)
def start_message(message):
    if 'youtu' in message.text:
      global link
      link = message.text
      bot.delete_message(message.chat.id,message.id)
      yt = YouTube(link).streams

      ls=[]
      for i in range(len(yt)):
        sstr=str(yt[i])
        try:
          if 'mime_type="video/mp4"' in sstr:
            nextt=sstr[sstr.index('res="')+5:]
            if (nextt[:4] not in ls) and str(nextt[:4])[-1]=='p':
              ls.append(nextt[:3])
        except:
          pass
      ls=list(set(ls))
      ls.sort()
      markup = telebot.types.InlineKeyboardMarkup()

      count=len(ls)//3
      run=0
      while True:
          if count==0:
              break
          markup.add(telebot.types.InlineKeyboardButton(text=ls[run]+'p 📹', callback_data=ls[run]),telebot.types.InlineKeyboardButton(text=ls[run+1]+'p 📹', callback_data=ls[run+1]),telebot.types.InlineKeyboardButton(text=ls[run+2]+'p 📹', callback_data=ls[run+2]))
          run+=3
          count-=1
      if (len(ls)-run)==1:
          markup.add(telebot.types.InlineKeyboardButton(text=ls[run]+'p 📹', callback_data=ls[run]))
      else:
          markup.add(telebot.types.InlineKeyboardButton(text=ls[run]+'p 📹', callback_data=ls[run]),telebot.types.InlineKeyboardButton(text=ls[run+1]+'p 📹', callback_data=ls[run+1]))

      if yt.filter(type='audio'):
          markup.add(telebot.types.InlineKeyboardButton(text='Audio 🎵', callback_data='audio'))
      bot.send_message(message.chat.id, text=link, reply_markup=markup)
    else:
      bot.send_message(message.chat.id, text="Please send youtube link.")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Accepted! Wait.')
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    if call.data == 'audio':
        YouTube(link).streams.filter(type='audio').first().download('video')
        list_of_files = glob.glob('video//*')
        mp3 = open(max(list_of_files, key=os.path.getctime), "rb")
        try:
            bot.send_audio(call.message.chat.id, mp3,caption = f"<a href = '{link}'>{YouTube(link).streams[0].title}</a>",parse_mode = "HTML")

        except:
            bot.send_message(call.message.chat.id, 'It is so large file sorry 😢. ')
    else:
        call.data+='p'
        YouTube(link).streams.filter(res=call.data,file_extension='mp4').first().download('video')
        video = open(max(glob.glob('video//*'), key=os.path.getctime), "rb")
        try:
            bot.send_video(call.message.chat.id, video,caption = f"<a href = '{link}'>{YouTube(link).streams[0].title}</a>",parse_mode = "HTML",timeout=10000)
        except:
            bot.send_message(call.message.chat.id, 'It is so large file sorry 😢.')
    os.remove(min(glob.glob('video//*'), key=os.path.getctime))
bot.infinity_polling()

