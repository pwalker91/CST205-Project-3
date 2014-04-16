#Name: Aaron Haycraft
#Date: 2/12/14
#Objective: To manipulate audio, and to play clips of an audio file in separate segments.

#soundExplore() is a starter function
def soundExplore():
  fileName=pickAFile()
  aSound=makeSound(fileName)
  print "Information about aSound", aSound
  print "Getting first sample:", getSampleValueAt(aSound, 0)
  print "Getting the length:", getLength(aSound)
  print "Getting sampling rate:", getSamplingRate(aSound)
  play(aSound)
  blockingPlay(aSound)
  playAtRate(aSound,2.0)
  explore(aSound)
  return aSound
  
#returnSound() will initialize a sound file
def returnSound():
  filename=pickAFile()
  newSound=makeSound(filename)
  print getLength(newSound)
  return newSound
  
#increaseVolume() increases volume of a sound
def increaseVolume(sound):
   for sample in getSamples(sound):
     value =getSampleValue(sample)
     setSampleValue(sample,value*2)
  
#increaseVolume2() increases volume of a sound in a different way than the first function
def increaseVolume2(sound):
  for index in range(0, getLength(sound)):
    value =getSampleValueAt(sound,index)
    setSampleValueAt(sound,index,value*2)
    
#changeVolume() changes the volume of a sound to a particular factor
def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
    
#increaseRange() creates three empty sound files, and will have three clips of a sound file stored in them.
#blockingPlay() is used so that the sounds can be played sequentially, not at the same time.
def increaseRange(sound):
  soundValue = 0
  first = int(getLength(sound)/3)
  second = int(2*getLength(sound)/3)  
  file1 = makeEmptySound(first, 44100)
  file2 = makeEmptySound(second, 44100)
  file3 = makeEmptySound(getLength(sound), 44100)
  
  for sample in range(0, first):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(file1, sample, value*200)
  
  for sample in range(first-1, second):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(file2, sample, value*200)
  
  for sample in range(second-1, getLength(sound)):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(file3, sample, value*200)
  
  blockingPlay(file1)
  blockingPlay(file2)
  blockingPlay(file3)      
  
  