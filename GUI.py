#!/usr/bin/python

from Recorder import Recorder
from SpeechToText import speech_to_text
from TextTranslator import translate_text

from Tkinter import *
#from Tkinter import ttk 
import ttk

filename = '/tmp/recorder.wav'
context = {}

def start(*args):
#	print(fromOptions[fromLanguage.get()])
	context['recorder'] = Recorder(filename)
	context['recorder'].start()
    
def stop(*args):
	context['recorder'].stop()
	text.set(speech_to_text(fromOptions[fromLanguage.get()],filename))
	translatedText.set(translate_text(toOptions[toLanguage.get()],text.get()))


root = Tk()
root.title("Universal Translator")
root.geometry("480x480")

mainframe = Frame(root) 
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.grid(column=0, row=0)
#mainframe.columnconfigure(0, weight=1)
#mainframe.rowconfigure(0, weight=1)

text = StringVar()
translatedText = StringVar()
fromLanguage = StringVar()
toLanguage = StringVar()




#fromOptions = { 'English' : 'en-US', 'French' : 'fr-FR', 'Spanish': 'es-MX' }
fromOptions = {
'Arabic (Iraq)' : 'ar-IQ',
'Chinese, Mandarin (Simplified, Hong Kong)' : 'cmn-Hans-HK',
'English (United States)' : 'en-US',
'French (France)' : 'fr-FR',
'German (Germany)' : 'de-DE',
'Hebrew (Israel)' : 'he-IL',
'Hindi (India)' : 'hi-IN',
'Italian (Italy)' : 'it-IT',
'Japanese (Japan)' : 'ja-JP',
'Korean (South Korea)' : 'ko-KR',
'Russian (Russia)' : 'ru-RU',
'Spanish (Mexico)' : 'es-MX'
}

#toOptions   = { 'English' : 'en', 'French' : 'fr', 'Spanish': 'es' }

toOptions = {
'Arabic (Iraq)' : 'ar',
'Chinese, Mandarin (Simplified, Hong Kong)' : 'cmn-Hans',
'English (United States)' : 'en',
'French (France)' : 'fr',
'German (Germany)' : 'de',
'Hebrew (Israel)' : 'he',
'Hindi (India)' : 'hi',
'Italian (Italy)' : 'it',
'Japanese (Japan)' : 'ja',
'Korean (South Korea)' : 'ko',
'Russian (Russia)' : 'ru',
'Spanish (Mexico)' : 'es'
}



#text.set("Hello, my name is Adam and I love cheesy potatos!  They are super cheesy and yummy.  How good is that?!")

fromMenu = OptionMenu(mainframe, fromLanguage, *sorted(fromOptions.keys()))
toMenu = OptionMenu(mainframe, toLanguage, *sorted(toOptions.keys()))
fromLanguage.set('English (United States)')
toLanguage.set('Spanish (Mexico)')

Button(mainframe, text="Start Recording", command=start, width=25, height=3).grid(column=1, row=1, sticky=(N,S,W,E))
Button(mainframe, text="Stop Recording", command=stop,   width=25, height=3).grid(column=2, row=1, sticky=(N,S,W,E))

fromMenu.grid(column=1, row=2, sticky=(N,W))
Label(mainframe, textvariable=text, wraplength=470).grid(column=1, row=3, columnspan=2, sticky=W)
ttk.Separator(mainframe).grid(column=1,row=4,columnspan=2, sticky=(E,W))

toMenu.grid(column=1, row=5, sticky=(N,W))
Label(mainframe, textvariable=translatedText, wraplength=470).grid(column=1,  row=6, columnspan=2,sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
