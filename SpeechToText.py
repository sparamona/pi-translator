#!/usr/bin/python

## from https://cloud.google.com/speech-to-text/docs/basics

import base64
import requests
import urllib
import sys
import json

GOOGLE_KEY = 'YOUR_GOOGLE_KEY_HERE'
GOOGLE_URL = 'https://speech.googleapis.com/v1beta1/speech:syncrecognize'

def speech_to_text(bcp47LanguageCode, speech_file):
	url = GOOGLE_URL + '?' + urllib.urlencode( {'key' : GOOGLE_KEY } )
	with open(speech_file, 'rb') as speech:
        	# Base64 encode the binary audio file for inclusion in the JSON
        	# request.
        	speech_content = base64.b64encode(speech.read())
	body={ 
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                'sampleRate': 8000,     # 8 khz
                # See http://g.co/cloud/speech/docs/languages for a list of
                # supported languages.
                'languageCode': bcp47LanguageCode
            	},
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            }

	resp = requests.post(url,data=json.dumps(body))
	#print(resp)
	#print resp.text
	return resp.json()['results'][0]['alternatives'][0]['transcript']


#
#
#speech_to_text('sample.wav')


	
