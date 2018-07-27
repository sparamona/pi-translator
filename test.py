from Recorder import Recorder
from SpeechToText import speech_to_text
from TextTranslator import translate_text



recorder = Recorder('/tmp/out.wav')
recorder.start()
print ">>> Recording"
raw_input('press enter to stop ...')
recorder.stop()
print "<<< Stopped "
text = speech_to_text('es-MX', '/tmp/out.wav')
print text
translation = translate_text('en',text)
print translation
