# python-project-Text-to-Speech
This converts text to speech using the Python Programming Language 
Text-to-Speech Converter Using Tkinter
This project is a simple Text-to-Speech (TTS) converter built with Python, utilizing the Tkinter library for the graphical user interface and gTTS (Google Text-to-Speech) for converting text into audio. Users can input any text into the provided field, and with the click of a button, the text is converted into an MP3 file and played back automatically.

Features
Tkinter-based GUI: A minimalistic and user-friendly interface for easy interaction.
Text-to-Speech Conversion: Converts text entered by the user into speech using gTTS.
Audio Output: The generated speech is saved as an MP3 file and played back instantly.
Prerequisites
Make sure you have Python 3 installed on your system. This project is built using Python 3.13, but earlier versions of Python 3 should work as well.

The following Python libraries are required:

Tkinter: Built-in library for Python that provides tools to create graphical user interfaces.
gTTS: A Python library and CLI tool to interface with Google Translate's text-to-speech API.
os: A standard library that provides a way to interact with the operating system (used to play the audio file).

3. How to Use (tkinterwindow.py)
Input the text you want to convert into speech in the text field.
Click the "Change to Audio" button.
The text will be converted into an audio file (tkinterGUI.mp3) and played automatically.

The gTTS library is used to interact with Google Text-to-Speech and provides the core functionality for this project.
