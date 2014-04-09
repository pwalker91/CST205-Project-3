
## Making array of note frequencies based on piano key number (left to right, 0 to 88)
## The resulting frequencies are between 27.5 and 4186.01 Hz
def makeNotesArray():
    daNotes = {}
    for i in range(1,89):
        base = pow(2, (1.0/12))
        power = i-49
        freq = pow(base, power) * 440.0
        daNotes[i] = freq
    return daNotes


def go():
    import random
    import math
    
    ## Importing the picture
    path = pickAFile()
    printNow("Importing and reading picture")
    picture = makePicture(path)
    totalPixels = picture.getHeight() * picture.getWidth()
    
    daNotes = makeNotesArray()
    
    ## Calculating the total number of samples in this song, based
    length = int(raw_input("Please specify how long you want the song to be, in seconds: "))
    if length<1:
        length = int(raw_input("You must input a number greater than 1: "))
    rate = 44100 ## 44100 samples of the sound per second
    totalSamples = rate*length
    notesPerSecond = int(raw_input("Please specify how many notes per second you want played, between 2 and 16 (recommend 4 -> 10): "))
    if notesPerSecond>16 or notesPerSecond<2:
        notesPerSecond = int(raw_input("You must input a number greater than 2 and less than 16: "))
    sampsPerNote = int(rate/notesPerSecond)
    pixelsPerNote = int(totalPixels/(length*notesPerSecond))
    
    sound = makeEmptySound(totalSamples, rate)
    SAMPS = getSamples(sound)
    PIXS = getPixels(picture)

    ## This is where the sound starts (sample 0)
    lastIndex = 0
    lastPixelIndex = 0
    noteLow = 37#1
    noteHigh = 61#88
    printNow("Creating song from image...")
    
    ## While looping through the sound by lengths of notes
    ## Last index is increased at the end of the while
    
    while lastIndex<(totalSamples-sampsPerNote) and lastPixelIndex<(totalPixels-pixelsPerNote):
        ## This part analyzes the pixels between the last index used in the previous
        ## iteration and that index plus the number of pixels per note.
        ## The average is calculated, and then used to get the index of the note frequency
        pixelsValueTotal = 0
        for i in range(0, pixelsPerNote):
            pixel = PIXS[lastPixelIndex + i]
            pixelsValueTotal += float(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/(256*3)
        lastPixelIndex += pixelsPerNote
        noteIndex = int((pixelsValueTotal/pixelsPerNote)*(noteHigh-noteLow))
        noteFreq = daNotes[noteLow+noteIndex]
        
        ## Splitting up the samples into sections of how
        ## many waves per note, samples per wave, and sample per
        ## quarter wave
        numWavesPerNote = int( (1.0/notesPerSecond)*noteFreq )
        sampsPerWave = sampsPerNote/numWavesPerNote
        sampsPerQWave = sampsPerWave/4
        value = float(random.randint(22000,26000)) / sampsPerQWave
    
        for x in range(numWavesPerNote):
            ## Offset keeps track of which wave we are at
            offset = lastIndex + (x*sampsPerWave)
            
            ## ModValue is what is used to create the disipating wave form
            modValue = value * (pow((0.977742), x) + 0.2242)
            for j in range(sampsPerQWave):
                SAMPS[offset + (sampsPerQWave*0) + j ].value = int(modValue * j)
            for k in range(sampsPerQWave):
                SAMPS[offset + (sampsPerQWave*1) + k ].value = int(modValue * (sampsPerQWave-k))
            for m in range(sampsPerQWave):
                SAMPS[offset + (sampsPerQWave*2) + m ].value = int(-1 * modValue * m)
            for n in range(sampsPerQWave):
                SAMPS[offset + (sampsPerQWave*3) + n ].value = int(-1 * modValue * (sampsPerQWave-n))
    
        lastIndex += (x*sampsPerWave)

    ## Playing the sound. Stops when an input is taken. Then asks what to save the song as
    printNow("Playing song...")
    play(sound)
    stop = raw_input("Press Enter to Stop. ")
    if stop=="" or stop!="":
        stopPlaying(sound)
    
    ""
    ## This section shows the picture, and will "highlight" all of the pixels that are
    ## being used to generate a note. The note is then created and played
    show(picture)
    PIXS = getPixels(picture)
    correctPIXS = getPixels(picture)
    printNow("The image will show which pixels are being used the create the note played")
    printNow("Enter any text to stop")
    printNow("Press Enter to cycle to the next note...")
    for  x in range(0,(totalPixels/pixelsPerNote)):
        pixelsValueTotal = 0
        for i in range(0, pixelsPerNote):
            thisPix = PIXS[ (x*pixelsPerNote) + i]
            lastPix = PIXS[ ((x-1)*pixelsPerNote) + i]
            if int(x)>0:
                lastPix.setRed(correctPIXS[ ((x-1)*pixelsPerNote) + i].getRed())
                lastPix.setBlue(correctPIXS[ ((x-1)*pixelsPerNote) + i].getBlue())
                lastPix.setGreen(correctPIXS[ ((x-1)*pixelsPerNote) + i].getGreen())
            pixelsValueTotal += float(thisPix.getRed()+thisPix.getGreen()+thisPix.getBlue())/(256*3)
            thisPix.setRed(thisPix.getRed()+50)
            thisPix.setBlue(thisPix.getBlue()+50)
            thisPix.setGreen(thisPix.getGreen()+50)
        
        ## Getting the frequency for this section
        ## Setting the number of waves per note, samps per not
        pixelToNote = int((pixelsValueTotal/pixelsPerNote)*(noteHigh-noteLow))
        noteFreq = daNotes[noteLow+pixelToNote]
        lastIndex = 0
        note = makeEmptySound((rate*2), rate)
        noteSAMPS = getSamples(note)
        sampsPerWave = int((rate*2)/noteFreq)
        sampsPerQWave = sampsPerWave/4
        value = 25000 / sampsPerQWave
        for x in range(numWavesPerNote):
            ## Offset keeps track of which wave we are at
            offset = lastIndex + (x*sampsPerWave)
            
            ## ModValue is what is used to create the disipating wave form
            modValue = value * (pow((0.977742), x) + 0.2242)
            for j in range(sampsPerQWave):
                noteSAMPS[offset + (sampsPerQWave*0) + j ].value = int(modValue * j)
            for k in range(sampsPerQWave):
                noteSAMPS[offset + (sampsPerQWave*1) + k ].value = int(modValue * (sampsPerQWave-k))
            for m in range(sampsPerQWave):
                noteSAMPS[offset + (sampsPerQWave*2) + m ].value = int(-1 * modValue * m)
            for n in range(sampsPerQWave):
                noteSAMPS[offset + (sampsPerQWave*3) + n ].value = int(-1 * modValue * (sampsPerQWave-n))
    
        
        repaint(picture)
        play(note)
        """
        next = raw_input()
        if next != "":
            break
        """
    ""
    
    
    file = raw_input("Enter filename... ")
    if file!="":
        writeSoundTo(sound, "/Users/peterwalker/Desktop/"+file+".wav")
