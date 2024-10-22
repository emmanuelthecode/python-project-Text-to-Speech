#Text to Speech Converter using Python
from gtts import gTTS#This would import the gTTS module, a module that aids in the changing of text to audio data. 
import os #As we need many aspects of the operating system. This would allow us to utilize the ability of the operating system in order to output the audio file. 

text = "Emmanuel, this is your first audio file" #This is the text that would be outputted in an audio format. 
audio = gTTS(text = text, lang="en", slow=False)#This is the gTTS function where the text is the text that is supposed to be outputted as an audio file, the 'lang' is the language that is meant to be read. 
audio.save('first_audio.mp3')#It will be saved as this audio which will then be started by the os.system() function.
os.system('start first_audio.mp3')#This is used to start the text-to-audio.




