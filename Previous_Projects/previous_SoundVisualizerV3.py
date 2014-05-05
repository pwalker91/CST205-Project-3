def run():
   import random
   import string   ## USED TO GET FILE NAME
   import shutil   ## USED TO COPY AND DELETE IMAGES FOLDER
   
   save_path = "/Users/peterwalker/Documents/School/+ CSUMB Courses/CST 205/"
   desktop = "/Users/peterwalker/Desktop/"
   folder = "visualizer_images/"
   
      #This creates the folder at the specified location above
      # If the folder is already created, it will first delete it, then create it again
   try:
      os.makedirs(save_path+folder)
   except OSError:
      shutil.rmtree(save_path+folder)
      os.makedirs(save_path+folder)
   
   printNow("Please pick a sound")
   file = pickAFile()
   file_name = file[string.rfind(file,"/")+1:]
   SOUND = makeSound(file)
   rate = getSamplingRate(SOUND)
   SAMPLES = getSamples(SOUND)
   numSamples = getNumSamples(SOUND)
   
      #Declaring necessary numbers for loops and index counters
   framesPerSec = 25
   sampleSectionsPerFrame = 40
   lastSecondSectionCount = int( sampleSectionsPerFrame*(float(5)/8) )
   nextHalfSecondSectionCount = int( sampleSectionsPerFrame*(float(3)/8) )
      ## This is also how many pixels there will be per section
         # 21 Will divide nicely into the rate/framesPerSec if rate is 44100 or 22050
   pixelsPerSection = 21
   samplesPerSection = int( (rate/framesPerSec)/pixelsPerSection )
   sampleIndex = 0
   frameIndex = 0
   lastPercentage = 0
   
      #width and height of picture
   width = pixelsPerSection*sampleSectionsPerFrame
   height = 600
   
      #Finding the "loudest" sample in the given audio
   maxSampValue = 0
   for i in range(0, numSamples):
      if maxSampValue < SAMPLES[i].value:
         maxSampValue = SAMPLES[i].value
         
      #This will be multiplied into the sample value to give
      # the vertical amount that will be added to our line
   ratio = float(height/2)/maxSampValue
   
   printNow("Starting Visualization")
   
      #This is an array that will hold all of the y-coordinates
      # for the section of the picture
   averagesArray = [ [0]*pixelsPerSection ]*(lastSecondSectionCount+1)
   for a in range(lastSecondSectionCount+1, sampleSectionsPerFrame):
      toBeAppended = [0]*pixelsPerSection
      for b in range(0, pixelsPerSection):
         sampleAvg = 0
         for c in range(0, samplesPerSection):
            sampleAvg += SAMPLES[sampleIndex+c].value*ratio
         sampleIndex += samplesPerSection
         toBeAppended[b] = int( (float(sampleAvg)/samplesPerSection) )
      averagesArray.append(toBeAppended)
   
      #This while loop will iterate through the sound, creating the appropiate image for the
      # current section of time
   while sampleIndex<( numSamples+(samplesPerSection*(lastSecondSectionCount+nextHalfSecondSectionCount)) ):
      picture = makeEmptyPicture(width, height, black)
      soundColor = white
      lineColor = red
      currentPercentage = int((float(sampleIndex)/numSamples) *100)
      if currentPercentage != lastPercentage:
         printNow("Working.... "+str(currentPercentage)+"%")
         lastPercentage = currentPercentage
   
         #Adding the red line in the horizontal center of the pictures
      soundSyncLine = int((float(5)/8)*width)
      picture.addLine(lineColor, 0, (height/2), width, (height/2))
      picture.addLine(lineColor, soundSyncLine, 0, soundSyncLine, height)
      
         #Determining the array of averages for the 21 pixels in the new section.
         # first removes the first array (moved past it), then gets array, then appends
      averagesArray.pop(0)
      newAverages = [0]*pixelsPerSection
      for q in range(0, pixelsPerSection):
         sampleAvg = 0
         for r in range(0, samplesPerSection):
            try:
               sampleAvg += SAMPLES[sampleIndex+r].value*ratio
            except IndexError:
               sampleAvg += 0
         sampleIndex += samplesPerSection
         newAverages[q] = int( (float(sampleAvg)/samplesPerSection) )
      averagesArray.append(newAverages)
      
      
      #This is creating the image for this iteration
      for i in range(0, sampleSectionsPerFrame):
         for j in range(0, pixelsPerSection):
            thisX = (i*pixelsPerSection)+j
            nextX = (i*pixelsPerSection)+j+1
            try:
               picture.addLine(soundColor, thisX, (height/2)-averagesArray[i][j], nextX, (height/2)-averagesArray[i][j+1])
            except IndexError:
               try:
                  picture.addLine(soundColor, thisX, (height/2)-averagesArray[i][j], nextX, (height/2)-averagesArray[i+1][0])
               except IndexError:
                  Im_Doing_Something_Here = false
         ## END FOR
      ## END FOR
      
         #Iterate frame index before saving picture
      frameIndex += 1
         #This section is for naming the picture, and padding the appropiate number of 0's
      if frameIndex<10:
         writePictureTo(picture, save_path+folder+"frame0000"+str(frameIndex)+".jpg")
      elif frameIndex<100:
         writePictureTo(picture, save_path+folder+"frame000"+str(frameIndex)+".jpg")
      elif frameIndex<1000:
         writePictureTo(picture, save_path+folder+"frame00"+str(frameIndex)+".jpg")  
      elif frameIndex<10000:
         writePictureTo(picture, save_path+folder+"frame0"+str(frameIndex)+".jpg")
      else:
         writePictureTo(picture, save_path+folder+"frame"+str(frameIndex)+".jpg")
   ## END WHILE
   
   
      #This is where the movie is created
   printNow("Creating Movie")
   mov = makeMovieFromInitialFile(save_path+folder+"frame00001.jpg")
   writeAVI(mov, "/Users/peterwalker/Desktop/"+file_name[:-4]+".avi", framesPerSec)
   
   printNow("Would you like to copy the folder of images to the desktop?")
   response = raw_input("(y/n) ")
   while response != "y" and response != "n":
      printNow("You did not input 'y' or 'n'")
      response = raw_input("(y/n) ")
   
      ### MOVE IMAGES FOLDER WITH FILENAME APPENDED
   if response == 'y':
      try:
         shutil.copytree(save_path+folder, desktop+folder[:-1]+"_"+file_name[:10]+"/")
      except OSError:
         moved = false
   
      ### DELETEING IMAGES FOLDER
   try:
      shutil.rmtree(save_path+folder)
   except OSError:
      deleted = false



