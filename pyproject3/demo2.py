from gtts import gTTS
import os 
#This program is going to be used to read text from a file and output it as an audio. 

text_being_read = open('demo.txt', 'r').read() #This would open the file to be read. 
language = 'en'

read_text = gTTS(text=text_being_read, lang=language, slow=False)
read_text.save('second_audio.mp3')
os.system('start second_audio.mp3')

