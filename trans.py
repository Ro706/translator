import os
from pyfiglet import Figlet
from translate import Translator
from tqdm import tqdm
import time
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
for i in tqdm(range(100)):
    time.sleep(0.0002)
os.system("mpv /data/data/com.termux/files/home/trans.mp3")


