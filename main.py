from musicalNotes import *
from generateNoteSequence import *
import time
import metronome
import piano

def displayTonicAndPlayScale(defaultScale = "MAJOR"):
    if defaultScale == "MAJOR":
        notes = music.getRandomMajorScale()
    elif defaultScale == "MINOR":
        notes = music.getRandomMinorScale()
    print("TONIC IS: "+str(notes[0]))
    print("SCALE NOTES ARE: " + str(notes))
    playScale(notes)
    return notes

def generateRhythmAndNotes(notes, numberOfNotes = 3):
    randomNotes = generateRandomNotes(notes, numberOfNotes)
    randomRhythm = generateRandomRhythm(numberOfNotes)
    return (randomNotes, randomRhythm)

def playGeneratedNotes(randomNotes, randomRhythm):
    print("PLAYING RANDOMLY GENERATED NOTES")
    sound = constructWaveFile(randomNotes, randomRhythm)
    play(sound)

def executeEarTrainingExercise(defaultScale = "MAJOR", pianoPromptLength = 20000, numberOfNotes = 3):
    notes, rhythm = generateRhythmAndNotes(displayTonicAndPlayScale(defaultScale), numberOfNotes)
    time.sleep(1)
    playGeneratedNotes(notes, rhythm)
    recordedNotes, metronomeTimeStamps = piano.main(pianoPromptLength)
    evaluateExerciseResponse(recordedNotes, metronomeTimeStamps, notes, rhythm)

def evaluateNoteRhythm(noteTimeStamps,rhythm, metronomeTimeStamps):
    for i in range(0, len(rhythm)-1):
        print(abs(noteTimeStamps[i+1] - (noteTimeStamps[i])))
        print(rhythm[i])
        if rhythm[i] == 1 and (abs(noteTimeStamps[i+1] - (noteTimeStamps[i]+1)) > 0.2):
            return False
        if rhythm[i] == 2 and (abs(noteTimeStamps[i+1] - (noteTimeStamps[i]+0.5)) > 0.2):
            return False
    return True

def evaluateExerciseResponse(recordedNotes, metronomeTimeStamps, notes, rhythm):
    playedNotes = []
    noteTimeStamps = []
    if recordedNotes != []:
        (playedNotes, noteTimeStamps) = list(map(list, zip(*recordedNotes)))
    if playedNotes != notes:
        print("INCORRECT ANSWER: YOU PLAYED " + str(playedNotes) + " BUT THE CORRECT ANSWER WAS " + str(notes))
    else:
        if evaluateNoteRhythm(noteTimeStamps,rhythm, metronomeTimeStamps) == True:
            print("CORRECT ANSWER: " + str(notes) + " " + noteRhythmToString(rhythm))
        else:
            print("THE RIGHT NOTES WERE PLAYED " + str(notes) + " BUT THE CORRECT RHYTHM IS " + noteRhythmToString(rhythm))

    

if __name__ == "__main__":
    music = musicalNotes()
    pianoPromptLength = 15000
    executeEarTrainingExercise("MAJOR", pianoPromptLength)
    
    


