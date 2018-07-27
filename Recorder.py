import alsaaudio
import time
from threading import Thread

DEVICE = 'plughw:1,0'

class Recorder(Thread):

    def __init__(self,filename):
        Thread.__init__(self)
        self._filename = filename
        self._stop = False

            
    def run(self):
        self._stop = False
        f = open(self._filename,'wb')

        inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK, device=DEVICE)
        inp.setchannels(1)
        inp.setrate(8000)
        inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        inp.setperiodsize(160)
	self._inp = inp

        while(self._stop == False):
            l,data = inp.read()
            if l:
                f.write(data)
                time.sleep(.001)
        f.close()

    def stop(self):
        self._stop = True
	time.sleep(1)


def record_file(filename):
	recorder = Recorder(filename)
	recorder.start()
	print ">>> Recording"
	raw_input('press enter to stop ...')
	recorder.stop()
	print "<<< Stopped recording"
	time.sleep(1)


#r = Recorder('/tmp/out.wav')
#r.start()
#print 'starting 5 sec'
#time.sleep(5)
#print 'finished with 5 sec'
#r.stop()
#time.sleep(1)
