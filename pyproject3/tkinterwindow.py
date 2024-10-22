#This is a section of code that converts text into audio through the use of the Tkinter interface. 
from tkinter import * #Importing the main parts of the tkinter library.
import os 
from gtts import gTTS 


def changeToAudio():#This is a method that would be called by the button. When it is called, all data that has been entered in the Entry would be converted into an mp3 file in order to convert from text to audio. 
    entry = user_entry.get()#This 'entry' gets the data that was input in the user_entry. 
    changed_audio=gTTS(text=entry, lang="en", slow=False)#This changes the text to audio through the use of the gTTS module. 
    changed_audio.save('tkinterGUI.mp3')#This saves it as an mp3 file which can then be played by the system.
    os.system('start tkinterGUI.mp3')#This is a method done by the system which aids in the playing of the now changed text to audio.


window = Tk()
window.geometry("300x100")#Changes the size of the window


label_1 = Label(window, text="Please input your text:")#The label that would reference where the txt should be inputted. 
user_entry = Entry(window)#The entry of the user. 
button_1 = Button(text = "Change to Audio", command=changeToAudio)#The button that would be clicked in order to call a function  which then converts it from text to audio. 


label_1.grid(row=0, column=0)
user_entry.grid(row=0, column=1)
button_1.grid(row=1, column=1)




window.mainloop()