from music21 import *
from music21.interval import Interval
from music21.stream import Stream


#verify species 1 counterpoint
#melody1 is a music21.stream.Stream of the cantus firumus, melody2 is the secondary melody
def verifyCounterpointVerbose(melody1: stream.Stream, melody2: stream.Stream) -> bool:

    rval = True
    allowedVerticalIntervals = {"P1", "m3", "M3", "P5", "m6", "M6", "P8"}
    allowedHorizontalIntervals = {"P1","m2", "M2", "m3", "M3", "P4", "P5", "m6", "M6", "P8"}

    melody1 = melody1.flat.notes
    melody2 = melody2.flat.notes
    final = melody1[-1]

    if melody1.duration != melody2.duration:
        print("Durations do not match up")
        return False

    if melody2.flat.notes[-1].pitch.pitchClass != final.pitch.pitchClass:
        print("Don't end on same note:", melody1[-1], melody2[-1])
        rval = False

    if not  (melody2[0].pitch.pitchClass == final.pitch.pitchClass or interval.pitch.Interval(melody2[0], final).name == 'P5'):
        print("Melody 2 starts on {}, not on the final or a P5 to the final {}.", melody2[0].name, final)
        rval = False


    badVerticalIntervalList = []
    badHorIntM1 = []
    badHorIntM2 = []
    for i in range(len(melody1)):
            #check that all the intervals are okay
        if Interval(melody1[i], melody2[i]).name not in allowedVerticalIntervals:
            badVerticalIntervalList.append((i+1, Interval(melody1[i], melody2[i])))
            rval = False

        if i != 0 and Interval(melody2[i-1], melody2[i]).name not in allowedHorizontalIntervals:
            badHorIntM2.append((i-1, i, Interval(melody2[i-1], melody2[i])))


    if not len(badVerticalIntervalList) == 0:
        print("Bad vertical intervals:")
    for v in badVerticalIntervalList:
        print(v)

    if not len(badHorIntM2) == 0:
        print("Bad vertical intervals:")
    for v in badHorIntM1:
        print(v)

    return rval

def testVerify():
    s1 = Stream(converter.parse("tinyNotation: d1 a g f e d f e d'"))
    s2 = Stream(converter.parse("tinyNotation: d'1 c' b- a g f a c'# d'"))
    biggerStream = Stream()
    biggerStream.append(stream.Part(s1))
    biggerStream.append(stream.Part(s2))
    #biggerStream.show()

    verifyCounterpointVerbose(s1, s2)

if __name__ == "__main__":
    testVerify()