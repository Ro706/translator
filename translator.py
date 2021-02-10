import os
from translate import Translator
translator= Translator(to_lang="German")
translation = translator.translate(str(input("enter:")))
print (translation)
from gtts import gTTS
language = 'en'
output1=gTTS(text=translation,lang=language)
output1.save('trans.mp3')
os.system("mpv /data/data/com.termux/files/home/project/trans.mp3")

