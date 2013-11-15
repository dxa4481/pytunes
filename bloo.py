import numpy, math, scipy.io.wavfile, notes, random



def getTone(length, pitch, rest = False):
    tone = []
    toneLength = length * 44100
    for i in range(int(round(toneLength))):
        if(rest):
            tone.append(0)
        else:
            tone.append(math.sin(pitch * (2 * math.pi) * i / 44100))
    return tone
def getChipTone(length, pitch, ratio=1, rest=False, amp=1):
    tone = []
    toneLength = length * 44100
    upDown = False
    period = 44100/pitch
    for i in range(int(round(toneLength))):
        if i % (period) > period / 2 * ratio:
            upDown = False
        elif i % (period) > 0:
            upDown = True
        if(rest):
            tone.append(0)
        elif(upDown):
            tone.append(-1 * amp)
        else:
            tone.append(1 * amp)
    return tone
        
def scaleWrite(data,name):
    data = numpy.array(data)
    scaled = numpy.int16(data/numpy.max(numpy.abs(data)) * 32767)
    scipy.io.wavfile.write(name, 44100, scaled)


def bassInstrementSample(startAfter, approxLength, volume=1, shortestNote=.125, numNotes=9):
    sample = []
    brown = 1
    numIncNotes = random.randint(1,3)
    pause = getChipTone(startAfter, 1, 1, True, volume)
    for i in range(numNotes):
        if i % numIncNotes == 0:
            numIncNotes = random.randint(1,3)
            brownInc = random.randint(0,1)
            if brownInc == 0:
                brownInc = -1
        brown += brownInc
        if brown < 1:
            brown = 10
        if brown > 10:
            brown = 1
        sample += getChipTone(random.randint(1,4)*shortestNote, notes.cMajor(brown % 5, brown / 5 + 1, True), .5, False, .8)
    while (len(sample + pause) / 44100 < approxLength):
        sample += sample
    return pause + sample
def driftInstrementSample(startAfter, approxLength, volume=1, shortestNote=.2):
    sample = []
    brown = 1
    numIncNotes = random.randint(1,10)
    pause = getChipTone(startAfter, 1, 1, True, volume)
    i = 0
    while(len(sample) / 44100 < approxLength):
        if i % numIncNotes == 0:
            numIncNotes = random.randint(1,10)
            brownInc = random.randint(0,1)
            if brownInc == 0:
                brownInc = -1
        brown += brownInc
        if brown < 1:
            brown = 5
        if brown > 10:
            brown = 1
        sample += getChipTone(random.randint(1,10)*shortestNote, notes.cMajor(brown % 5, brown / 5 + 4, True), .5, False, 1)
    i += 1
    return pause + sample
def stitchToOne(sample1, sample2, sample3=[], sample4=[], sample5=[]):
    stitched = []
    for i in range(max(len(sample1), len(sample2), len(sample3), len(sample4), len(sample5))):
        sumI = 0
        if i < len(sample1):
            sumI += sample1[i]
        if i < len(sample2):
            sumI += sample2[i]
        if i < len(sample3):
            sumI += sample3[i]
        if i < len(sample4):
            sumI += sample4[i]
        if i < len(sample5):
            sumI += sample5[i]
        stitched.append(sumI)
    return stitched
sample1 = bassInstrementSample(0, 34)
sample2 = driftInstrementSample(4, 10)
sample3 = driftInstrementSample(14, 10, 1, .05)
sample4 = driftInstrementSample(24, 10)
stitched = stitchToOne(sample1, sample2, sample3, sample4)

scaleWrite(stitched,'test.wav')
#test2()
print('done!')


