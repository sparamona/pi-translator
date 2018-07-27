#!/usr/bin/python
from Recorder import record_file
from SpeechToText import speech_to_text
from TextTranslator import translate_text


# Three functions:
#
# 1.  record_file(<filename>)
#     records audio to the filename until the user hits enter
#
# 2.  speech_to_text(<languageCode>, <audio filename>)
#     converts the audio file to text using the language code provided.
#     Example language codes:
#	en-US - english-US
#	es-MX - spanish-Mexico
#       fr-FR - french-France
#     Returns the text
#
# 3. translate_text(<target language>, <text>)
#    translates the text to the target language
#    Example langauages are:
#      en - english
#      es - spanish
#      fr - french
#      de - german
#    Returns the translated text

record_file("recordfile")

text = speech_to_text("en-US", "recordfile")

print(text)

Adam = translate_text("es", text)

print(Adam)
