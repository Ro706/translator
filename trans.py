import os
from pyfiglet import Figlet
from translate import Translator
translator= Translator(to_lang="German")
os.system("clear")
f=Figlet(font ='slant')
print(f.renderText('translator'))
translation = translator.translate(str(input("enter:")))
print (translation)
from gtts import gTTS
language = 'en'
output1=gTTS(text=translation,lang=language)
output1.save('trans.mp3')
os.system("mpv /data/data/com.termux/files/home/trans.mp3")


