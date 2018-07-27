#!/usr/bin/python

import requests
import urllib
import sys

GOOGLE_KEY = 'YOUR_GOOGLE_KEY_HERE'
GOOGLE_TRANSLATE_URL = 'https://translation.googleapis.com/language/translate/v2'



#
# translate_text(target, text)
# This is the function that translates text to the 'target' language. 
# For a list of target languages, see the google translate documentation 
#
def translate_text(target, text):
	url = GOOGLE_TRANSLATE_URL + '?' + 'key=' + GOOGLE_KEY + '&target=' + target + '&q=' + text
	resp = requests.get(url)
	return resp.json()['data']['translations'][0]['translatedText']


#first argument is:   sys.argv[1]
#second argument is:  sys.argv[2]

#example 
#translate_text('es', 'Hello, my friend!  How are you today?')


	
