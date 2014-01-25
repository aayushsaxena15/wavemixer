import wave, pyaudio,time
import struct, sys
FORMAT = pyaudio.paInt16
stream=""
wf = ""
class IO:
    def __init__(self):
        pass

    def read_wave(self,fileName,waveObj):
        waveFile = wave.open(fileName, 'rb')
        waveObj.frameRate = waveFile.getframerate()
        waveObj.sampleWidth = waveFile.getsampwidth()
        waveObj.channels = waveFile.getnchannels()
        waveObj.originalLength = waveFile.getnframes()
        rawData = waveFile.readframes(waveObj.originalLength)
        totalLength =  waveObj.originalLength *  waveObj.channels
        fmt = "%ih" % (totalLength)
        waveObj.originalPcmData = list(struct.unpack(fmt, rawData))
        print len( waveObj.originalPcmData)
        print "read size"
        del rawData

    def make_wave(self,fileName,waveObj):
    
        fmt = "%ih" % (waveObj.length*waveObj.channels)
        print len(waveObj.pcmData)
        rawData = struct.pack(fmt, *(waveObj.pcmData))
        f = wave.open(fileName, 'wb')
        f.setframerate(waveObj.frameRate)
        f.setnframes(waveObj.length)
        f.setsampwidth(waveObj.sampleWidth)
        f.setnchannels(waveObj.channels)
        f.writeframes(rawData)
        f.close()
        del rawData

    def save_recorded(self,fileName,waveObj):
        f = wave.open(fileName, 'wb')
        f.setnchannels(1)
        f.setsampwidth(waveObj.pyAudioObj.get_sample_size(FORMAT))
        f.setframerate(16000)
        f.writeframes(waveObj.originalPcmData)
        f.close()

    
class MyWave:

    """MyWave class"""

    def __init__(self):
        """Constructor"""

        self.ampFactor=1
        self.timeShiftFactor=0
        self.timeScaleFactor=0
        self.reverse=False

        self.maxValue=32767
        self.minValue=-32768

        self.frameRate=16000
        self.sampleWidth=2
        self.channels=1
        self.length=1
        self.originalLength=1
        self.pcmData=[0]
        self.originalPcmData=[0]

        self.pyAudioObj=pyaudio.PyAudio()
        self.stream=""
        self.fPtr=""
        self.fileName=""

        self.recordFlag=False
        self.playFlag=True
        self.mixFlag=False
        self.modulateFlag=False

    def apply_changes(self):
        print len(self.originalPcmData)
        print "mayank apply"
        print self.ampFactor
        print self.timeShiftFactor
        print self.timeScaleFactor
        print self.reverse

        self.pcmData=self.originalPcmData
        print len(self.pcmData)
        self.length=self.originalLength
        self.amplitude_scale()
        self.time_shift()
        self.time_reversal()
        self.time_scale()

    def amplitude_scale(self):
        if self.ampFactor!=1:
            self.pcmData=[min(max(self.minValue,int(round(i*self.ampFactor))),self.maxValue) for i in self.pcmData]

    def time_shift(self):
        skipFrames=int(abs(self.timeShiftFactor))
        if(self.timeShiftFactor<0):
            self.pcmData=self.pcmData[skipFrames:]+[0]*skipFrames
        elif self.timeShiftFactor>0:
            self.pcmData=([0]*skipFrames)+self.pcmData[:-skipFrames]
        self.length=len(self.pcmData)

    def time_reversal(self):
        if self.reverse:
            self.pcmData=self.pcmData[::-1]

    def time_scale(self):
        if self.timeScaleFactor<0:
            temp=[]
            for i in self.pcmData:
                temp+=[i]*abs(self.timeScaleFactor)
            self.pcmData=temp
        elif self.timeScaleFactor>0:
             self.pcmData=self.pcmData[::self.timeScaleFactor]
        self.length=len(self.pcmData)

    def modulation_or_mixing(self,mod,wave1,wave2,wave3):
        # 0 for modulation 1 for mixing
        if mod > 1 or mod < 0:
            raise ValueError("Invalid Mode")
        op=['*','+'][mod]
        tempWave1=MyWave()
        tempWave2=MyWave()
        tempWave3=MyWave()
        tempWave1.copy_wave(wave1)
        tempWave2.copy_wave(wave2)
        tempWave3.copy_wave(wave3)
        print "modu upar"
        print tempWave1.length
        print wave1.length
        self.originalLength=max(tempWave1.length,tempWave2.length,tempWave3.length)
        self.length=self.originalLength
        print "----modulation-----"
        print self.length
        tempWave1.append_data(self.length)
        tempWave2.append_data(self.length)
        tempWave3.append_data(self.length)
        self.originalPcmData=[min(max(self.minValue,int(round(eval(str(tempWave1.pcmData[i])+op+str(tempWave2.pcmData[i])+op+str(tempWave3.pcmData[i]))))),self.maxValue) for i in range(0,self.length) ]
        del tempWave1
        del tempWave2
        del tempWave3

    def copy_wave(self,source):
        self.ampFactor=source.ampFactor
        self.timeShiftFactor=source.timeShiftFactor
        self.timeScaleFactor=source.timeScaleFactor
        self.reverse=source.reverse
        self.length=source.length
        self.originalLength=source.originalLength
        self.pcmData=source.pcmData
        self.originalPcmData=source.originalPcmData

    def append_data(self,newLength):
        print "append"
        print newLength
        print self.length
        self.pcmData=self.pcmData*(newLength/self.length)+self.pcmData[:(newLength%self.length)]
        self.length=len(self.pcmData)

    def callback_play(self,in_data, frame_count, time_info, status):
        data = self.fPtr.readframes(frame_count)
        if self.playFlag==False:
            return (data,pyaudio.paAbort)
        return (data, pyaudio.paContinue)

    def play_wave(self):
        self.stream=""
        self.pyAudioObj.terminate()
        self.pyAudioObj=pyaudio.PyAudio()
        self.playFlag=True
        print "mayank play wave"
        print len(self.pcmData)
        """
        self.stream=self.pyAudioObj.open(format=self.sampleWidth,
                                        channels=self.channels,
                                        rate=self.frameRate,
                                        output=True,
                                        stream_callback=self.callback_play)
        """
        self.stream = self.pyAudioObj.open(format=self.pyAudioObj.get_format_from_width(self.fPtr.getsampwidth()),channels=self.fPtr.getnchannels(),rate=self.fPtr.getframerate(),output=True,stream_callback=self.callback_play)
    

    def stop_playing(self):
        self.playFlag=False
        self.stream=""
        self.pyAudioObj.terminate()
        self.pyAudioObj=pyaudio.PyAudio()

    def callback_record(self,in_data, frame_count, time_info, status):
        self.originalPcmData+=in_data
        if self.recordFlag==False:
            return (in_data,pyaudio.paAbort)
        return (in_data, pyaudio.paContinue)

    def record_wave(self):
        self.originalPcmData=""
        self.stream=""
        self.pyAudioObj.terminate()
        self.pyAudioObj=pyaudio.PyAudio()
        self.playFlag=True
        print "mayank record wave"
        print len(self.pcmData)
        self.stream=self.pyAudioObj.open(format=FORMAT,
                                        channels=1,
                                        rate=16000,
                                        input=True,
                                        stream_callback=self.callback_record)

    def stop_recording(self):
        self.recordFlag=False
        self.stream=""
        self.pyAudioObj.terminate()
        self.pyAudioObj=pyaudio.PyAudio()


if __name__=="__main__":
    io=IO();
    wave1=MyWave();
    wave2=MyWave();
    wave3=MyWave();
    modulatedWave=MyWave();
    mixedWave=MyWave();
    file1=sys.argv[1]
    file2=sys.argv[2]
    if(file1):
        io.read_wave(file1,wave1)
        print "main size"
        print len(wave1.originalPcmData)
#        wave1.ampFactor=2
#        wave1.amplitude_scale()
#        print wave1.frameRate
#        wave1.reverse=True
#        wave1.time_reversal()
        wave1.timeScaleFactor=-2
#        wave1.time_scale()
        
    if(file2):
        io.read_wave(file2,wave2)
        print "main size"
        print len(wave2.originalPcmData)
#        wave2.ampFactor=2
#        wave2.amplitude_scale()
#        print wave2.frameRate
        #wave1.reverse=True
        #wave1.time_reversal()
#        wave2.timeScaleFactor=2
#        wave2.time_scale()
#    wave1.pyAudioObj = pyaudio.PyAudio()
#    wave2.pyAudioObj = pyaudio.PyAudio()
#    mixedWave.pyAudioObj = pyaudio.PyAudio()
    
#    wave3.pcmData=[1]
#    modulation_or_mixing(0,wave1,wave2,wave3,modulatedWave)
    wave1.apply_changes()
    io.make_wave("wav1.wav",wave1)
    wave1.fPtr = wave.open("wav1.wav", 'rb')
    
    wave2.apply_changes()
    io.make_wave("wav2.wav",wave2)
    wave2.fPtr = wave.open("wav2.wav", 'rb')
    
    
    mixedWave.modulation_or_mixing(1,wave1,wave2,wave3)
    print "-----------------"
    print mixedWave.length
    print mixedWave.originalLength
    print "-----------------"
    mixedWave.apply_changes()
    io.make_wave("mix.wav",mixedWave)
    mixedWave.fPtr = wave.open("mix.wav", 'rb')


    wave1.play_wave()
    wave1.stream.start_stream()
#    time.sleep(0.1);
#    wave1.playFlag=False

#    wave2.play_wave()
#    wave2.stream.start_stream()
#    time.sleep(0.1);
#    wave2.playFlag=False

#    mixedWave.play_wave()
#    mixedWave.stream.start_stream()

    print "mayank"
    
#    make_wave("try.wav",wave2)
#    play_wave("try.wav")
#    make_wave("try.wav",modulatedWave)
#    play_wave("try.wav")
#    make_wave("try.wav",mixedWave)
#    play_wave("try.wav")
    while wave1.stream.is_active():
        time.sleep(0.1);
#    while mixedWave.stream.is_active():
#        time.sleep(0.1);
