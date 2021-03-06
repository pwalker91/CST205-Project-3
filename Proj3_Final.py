
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Scrollable File Contents Viewer class
class FileContentsViewer(swing.JFrame):
   import os
   import java
   import sys
   
   # ----------------
   # Class vars
   currentDirectory = ""
   files = None
   newpicture = None
   currentPicturePath = ""
   pictureExts = ["jpg","jpeg","gif","png","JPG","JPEG","GIF","PNG"]
   soundExts = ["wav", "WAV"]
   # ----------------
   
   # DESC: Initialization of the frame. Creates the buttons and file list
   #
   # INPUTS:   directory, String of directory on computer
   # OUTPUTS:  JFrame
   def __init__(self, directory=""):
      swing.JFrame.__init__(self, title="File Contents Viewer", size=(800,600))
      self.setLocationByPlatform(true)
      self.contentPane.layout = java.awt.BorderLayout()
      #Setting up the scroll list of files that can be used by the programs
      self.currentDirectory = directory
      filesList = self.listFilesInDirectory(self.currentDirectory)
      self.files = swing.JList(filesList)
      pane = swing.JScrollPane(self.files, name="ScrollPane", size=(400,200))
      self.contentPane.add(pane, java.awt.BorderLayout.CENTER)
      #Adding a button that will let the user view the file they are choosing
      fileView = swing.JButton("View Contents", name="FileView", actionPerformed = self.fileView)
      self.contentPane.add(fileView, java.awt.BorderLayout.WEST)
      #Adding a button that will allow the user to change the directory they are viewing
      changeDir = swing.JButton("Change Directory", name="ChangeDir", actionPerformed = self.changeDirectory)
      self.contentPane.add(changeDir, java.awt.BorderLayout.SOUTH)
      #Adding a text header, showing the user where they current are located
      dirHeader = swing.JLabel(self.currentDirectory, swing.JLabel.CENTER, name="Header")
      self.contentPane.add(dirHeader, java.awt.BorderLayout.NORTH)
      #Adding a sub-Panel that will have the buttons that can be used to alter/manipulate the files
      smallFrame = swing.JPanel(java.awt.GridLayout(0,1), name="ButtonGrid")
      smallFrame.add(swing.JButton("Aaron's First Project", actionPerformed=self.Aaron_First_Project))
      smallFrame.add(swing.JButton("Aaron's Second Project", actionPerformed=self.Aaron_Second_Project))
      smallFrame.add(swing.JButton("Peter's First Project", actionPerformed=self.Peter_First_Project))
      smallFrame.add(swing.JButton("Peter's Second Project", actionPerformed=self.Peter_Second_Project))
      smallFrame.add(swing.JButton("Some Fun Picture Filters", actionPerformed=self.filtersMenu))
      #smallFrame.add(swing.JButton("TEST", actionPerformed=self.testing))
      self.contentPane.add(smallFrame, java.awt.BorderLayout.EAST)
      #Showing the GUI
      self.pack()
      self.visible = true
   #END DEF
   
   
   # DESC: Uses the chosen file (in the frame list) and either opens it or plays it
   #
   # INPUTS:   none
   # OUTPUTS:  showing the chosen file
   def fileView(self, event=""):
      selected = self.files.getSelectedIndices()
      selectedFile = self.files.getModel( ).getElementAt( selected[0])
      selectedFile = self.currentDirectory+ "/"+ selectedFile
      fileExt = selectedFile.split(".")[-1]
      if (fileExt in self.pictureExts):
         pic = makePicture(selectedFile)
         openPictureTool(pic)
      #END IF
      if (fileExt in self.soundExts):
         snd = makeSound(selectedFile)
         openSoundTool(snd)
      #END IF
   #END DEF
   
   
   # DESC: Change's the frame's directory, and re-declares some swing components
   #
   # INPUTS:   none
   # OUTPUTS:  none
   def changeDirectory(self, event=""):
      components = self.contentPane.getComponents()
      index = 0
      for elem in components:
         if elem.getName() == "ScrollPane":
            index = components.index(elem)
      self.contentPane.remove(index)
      filesList = self.listFilesInDirectory()
      self.files = swing.JList(filesList)
      pane = swing.JScrollPane(self.files, name="ScrollPane", size=(400,200))
      self.contentPane.add(pane, java.awt.BorderLayout.CENTER)
      components = self.contentPane.getComponents()
      index = 0
      for elem in components:
         if elem.getName() == "Header":
            index = components.index(elem)
      self.contentPane.remove(index)
      dirHeader = swing.JLabel(self.currentDirectory, swing.JLabel.CENTER, name="Header")
      self.contentPane.add(dirHeader, java.awt.BorderLayout.NORTH)
      self.pack()
      self.visible = true
   #END DEF
   
   
   # DESC: This returns a list of .jpg or .wav files in either a given or chosen directory
   #
   # INPUTS:   directory, a String that can be empty, or a directory on the computer
   # OUTPUTS:  list, an array of file names
   def listFilesInDirectory(self, directory = ""):
      if directory == "":
         chooser = swing.JFileChooser()
         chooser.setFileSelectionMode(swing.JFileChooser.DIRECTORIES_ONLY)
         chooser.setApproveButtonText("Select Folder")
         chooser.setDialogTitle("Select Folder to Show File List")
         val = None
         cancelCount = 0
         val = chooser.showDialog(self, None)
         if (val == swing.JFileChooser.CANCEL_OPTION):
            if (self.currentDirectory == ""):
               if os.path.isdir( os.path.expanduser("~")+"/Desktop" ):
                  self.currentDirectory = os.path.expanduser("~")+"/Desktop"
               else:
                  self.currentDirectory = os.path.expanduser("~")+"/desktop"
               #END IF/ELSE
            else:
               keeping_the_current_directory = true
            #END IF/ELSE
         else:
            self.currentDirectory = str(chooser.getSelectedFile())
         #END IF/ELSE
      else:
         self.currentDirectory = directory
      #END IF/ELSE
      tempFilesList = os.listdir(self.currentDirectory)
      toRemove = []
      for entry in tempFilesList:
         if ((entry[0:1] == ".") or 
             (os.path.isdir(self.currentDirectory+"/"+entry)) or
             ( (entry.split(".")[-1] not in self.pictureExts) and (entry.split(".")[-1] not in self.soundExts) )
            ):
            toRemove.append(entry)
         #END IF
      #END FOR
      for removing in toRemove:
         tempFilesList.remove(removing)
      #END FOR
      return tempFilesList
   #END DEF
   
   
   # DESC: Used for debugging this Object
   #
   # INPUTS:   none
   # OUTPUTS:  a JFrame window with some simple text
   def testing(self, event="", text=""):
      mywindow = swing.JFrame(title="TEST OUTPUT",size=(600,100))
      mywindow.setLocationByPlatform(true)
      mywindow.contentPane.layout = java.awt.FlowLayout(java.awt.FlowLayout.CENTER)
      mywindow.contentPane.add(swing.JTextField(str(text)))
      mywindow.visible = true
   #END DEF


   # DESC: This creates a GUI with which the user can choose a filter with which
   #       to alter their image. If they like their new image, they can click save
   #
   # INPUTS:   none
   # OUTPUTS:  JFrame with filter buttons
   def filtersMenu(self, event=""):
      import string   ## USED TO GET FILE NAME, AND DO SOME OTHER STRING MANIPULATION
      #Getting the file chosen
      selected = self.files.getSelectedIndices()
      selectedFile = self.files.getModel( ).getElementAt( selected[0])
      selectedFile = self.currentDirectory + "/"+ selectedFile
      file_name = selectedFile[selectedFile.rfind("/")+1:]
      #Checking that the file is a picture file
      fileExt = file_name.split(".")[-1]
      if (fileExt not in self.pictureExts):
         mywindow = swing.JFrame(size=(600,100))
         mywindow.contentPane.layout = java.awt.FlowLayout(java.awt.FlowLayout.CENTER)
         mywindow.contentPane.add(swing.JLabel(file_name+" is not a picture file"))
         mywindow.setLocationByPlatform(true)
         mywindow.visible = true
         return None
      self.currentPicturePath = selectedFile
      # --------------------
      newFrame = swing.JFrame(title="Picture Filters Galore!", size=(650,200))
      newFrame.contentPane.layout = java.awt.BorderLayout()
      buttons = swing.JPanel(java.awt.GridLayout(0,2))
      saveButtons = swing.JPanel(java.awt.GridLayout(0,3))
      buttons.add(swing.JButton("Black and White Contrast", actionPerformed=self.BlackAndWhite))
      buttons.add(swing.JButton("Grayscale the photo", actionPerformed=self.grayscale))
      buttons.add(swing.JButton("Swap Red, Green, or Blue", actionPerformed=self.redGreenBlueSwap))
      buttons.add(swing.JButton("Make the negative of the photo", actionPerformed=self.negativeFlip))
      buttons.add(swing.JButton("Make the photo all one color", actionPerformed=self.singleColorScale))
      buttons.add(swing.JButton("Pixelize the photo", actionPerformed=self.pixelizeME))
      buttons.add(swing.JButton("Mirror the photo", actionPerformed=self.mirrorOnAxis))
      saveButtons.add(swing.JButton("Show Picture", actionPerformed=self.refresh))
      saveButtons.add(swing.JButton("Show Original", actionPerformed=self.refreshOrig))
      saveButtons.add(swing.JButton("Save Picture", actionPerformed=self.savePicture))
      newFrame.contentPane.add(buttons, java.awt.BorderLayout.CENTER)
      newFrame.contentPane.add(saveButtons, java.awt.BorderLayout.SOUTH)
      newFrame.setLocationByPlatform(true)
      newFrame.visible = true
   #END DEF
   
   
   # DESC: This refreshes the picture being shown
   def refresh(self, event=""):
      if self.newpicture is not None:
         repaint(self.newpicture)
      return None
   #END DEF
   
   # DESC: This refreshes the picture being shown
   def refreshOrig(self, event=""):
      repaint(makePicture(self.currentPicturePath))
      return None
   #END DEF
   
   # DESC: This writes the current picture in self.picture into the current directory
   def savePicture(self, event=""):
      from datetime import datetime
      fmt = '%Y%m%d-%I%M%S'
      now = datetime.now()
      d_string = now.strftime(fmt)
      import string
      before = self.currentPicturePath[:self.currentPicturePath.rfind(".")]
      after = self.currentPicturePath[self.currentPicturePath.rfind("."):]
      filePath = before + "_" + d_string + after
      writePictureTo(self.newpicture, filePath)
   #END DEF




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# OUR PREVIOUS PROJECTS ARE FUNCTIONS BELOW
   # DESC: Uses selected audio file to create a picture. Will then create a video of the picture creating itself.
   #
   # INPUTS:   .wav file from directory list
   # OUTPUTS:  picture of audio file, video creating picture of audio file
   def Aaron_First_Project(self, event=""):
      import string   ## USED TO GET FILE NAME
      #Getting the file chosen
      selected = self.files.getSelectedIndices()
      selectedFile = self.files.getModel( ).getElementAt( selected[0])
      selectedFile = self.currentDirectory + "/"+ selectedFile
      file_name = selectedFile[selectedFile.rfind("/")+1:]
      #Checking that the file is a wav file
      fileExt = file_name.split(".")[-1]
      if (fileExt not in self.soundExts):
         mywindow = swing.JFrame(size=(600,100))
         mywindow.contentPane.layout = java.awt.FlowLayout(java.awt.FlowLayout.CENTER)
         mywindow.contentPane.add(swing.JLabel(file_name+" is not a wav file"))
         mywindow.setLocationByPlatform(true)
         mywindow.visible = true
         return None
      dir=self.currentDirectory+'\\pictures\\'
      if not os.path.exists(dir):
        os.makedirs(dir)
      # --------------------
      #Variable declaration
      x=0
      y=0
      value=0
      data = 300
      picture=makeEmptyPicture(data,data)
      sound=makeSound(selectedFile)
      overall=(getNumSamples(sound))/(data*data)
      int(overall)
      pixelArray=getPixels(picture)
      pixelIndex=0
      for k in range (0, data):
        for i in range (0, data):
          total=0
          for j in range (0, overall):
            total+=getSampleValueAt(sound, ((k*overall*data)+(i*overall)+j))
          #END FOR J
          avg=total/overall
          if (avg<-50):
            pixelArray[pixelIndex].setColor(red)
          elif(avg<-25 and avg>=-50):
            pixelArray[pixelIndex].setColor(green)
          elif(avg<0 and avg>=-25):
            pixelArray[pixelIndex].setColor(blue)
          elif(avg<25 and avg>=0):
            pixelArray[pixelIndex].setColor(yellow)
          elif(avg<50 and avg>=25):
            pixelArray[pixelIndex].setColor(magenta)
          elif(avg>=50):
            pixelArray[pixelIndex].setColor(orange)
          #END IF/ELIF/ELIF
          pixelIndex+=1
        #END FOR I
        value=value+1
        if(value<10):
          writePictureTo(picture, dir+'photo000'+str(value)+'.jpg')
        elif(value<100):
          writePictureTo(picture, dir+'photo00'+str(value)+'.jpg')
        elif(value<1000):
          writePictureTo(picture, dir+'photo0'+str(value)+'.jpg')
        else:
          writePictureTo(picture, dir+'photo'+str(value)+'.jpg')
        #END IF/ELIF/ELSE
      #END FOR K
      #Shows final picture
      show(picture)
      mov = makeMovieFromInitialFile(dir+'photo0001.jpg')
      #Functions below will make and show movie.
      mov = makeMovieFromInitialFile(dir+'photo0001.jpg')
      print mov
      writeAVI(mov, dir+'newMovie.avi', 20)
      playMovie(mov)
   #END DEF
   
   
   # DESC: This function will take in a wav file, and will separate and speed up the audio sound in three different pieces.
   #
   # INPUTS:   .wav file
   # OUTPUTS:  The playing of sped up audio sounds.
   def Aaron_Second_Project(self, event=""):
      import string   ## USED TO GET FILE NAME
      #Getting the file chosen
      selected = self.files.getSelectedIndices()
      selectedFile = self.files.getModel( ).getElementAt( selected[0])
      selectedFile = self.currentDirectory + "/"+ selectedFile
      file_name = selectedFile[selectedFile.rfind("/")+1:]
      #Checking that the file is a wav file
      fileExt = file_name.split(".")[-1]
      if (fileExt not in self.soundExts):
         mywindow = swing.JFrame(size=(600,100))
         mywindow.contentPane.layout = java.awt.FlowLayout(java.awt.FlowLayout.CENTER)
         mywindow.contentPane.add(swing.JLabel(file_name+" is not a wav file"))
         mywindow.setLocationByPlatform(true)
         mywindow.visible = true
         return None
      # --------------------
      sound = makeSound(selectedFile)
      soundValue = 0
      #Creates values for different pieces of audio files and the files the audio will be stored in.
      first = int(getLength(sound)/3)
      second = int(2*getLength(sound)/3)  
      file1 = makeEmptySound(first, 44100)
      file2 = makeEmptySound(second, 44100)
      file3 = makeEmptySound(getLength(sound), 44100)
      #For loops for placing the new audio values in the new audio files
      for sample in range(0, first):
        value = getSampleValueAt(sound, sample)
        setSampleValueAt(file1, sample, value*200)
      #END FOR
      for sample in range(first-1, second):
        value = getSampleValueAt(sound, sample)
        setSampleValueAt(file2, sample, value*200)
      #END FOR
      for sample in range(second-1, getLength(sound)):
        value = getSampleValueAt(sound, sample)
        setSampleValueAt(file3, sample, value*200)
      #END FOR
      #Blocking play functions will separate the play of the audio files.
      blockingPlay(file1)
      blockingPlay(file2)
      blockingPlay(file3)
   #END DEF


   # DESC: This takes the user's chosen picture, and converts it into an audio file
   #
   # INPUTS:   picture file
   # OUTPUTS:  wav audio file
   def Peter_First_Project(self, event=""):
      import random
      import math
      import string   ## USED TO GET FILE NAME
      import shutil   ## USED TO COPY AND DELETE IMAGES FOLDER
      #Getting the file chosen
      selected = self.files.getSelectedIndices()
      selectedFile = self.files.getModel( ).getElementAt( selected[0])
      selectedFile = self.currentDirectory + "/"+ selectedFile
      file_name = selectedFile[selectedFile.rfind("/")+1:]
      #Checking that the file is a picture file
      fileExt = file_name.split(".")[-1]
      if (fileExt not in self.pictureExts):
         mywindow = swing.JFrame(size=(600,100))
         mywindow.contentPane.layout = java.awt.FlowLayout(java.awt.FlowLayout.CENTER)
         mywindow.contentPane.add(swing.JLabel(file_name+" is not a picture file"))
         mywindow.setLocationByPlatform(true)
         mywindow.visible = true
         return None
      continueThis = requestString("This function can take a while to run.\n" + 
                                    "Assume about 1 minute of processing per megabyte of data.\n" + 
                                    "Continue? (y/n)")
      if continueThis != "y":
         return None
      # --------------------
      ## Importing the picture and making the note array
      picture = makePicture(selectedFile)
      totalPixels = picture.getHeight() * picture.getWidth()
      daNotes = self.makeNotesArray()
      ## Calculating the total number of samples in this song, based
      length = requestIntegerInRange("Please specify how long you want the song to be, in seconds: ", 1, 5000)
      rate = 44100 ## 44100 samples of the sound per second
      totalSamples = rate*length
      notesPerSecond = requestIntegerInRange("Please specify how many notes per second you want played,\n"+
                                              " between 2 and 16 (recommend 4 -> 10): ", 2, 16)
      sampsPerNote = int(rate/notesPerSecond)
      pixelsPerNote = int(totalPixels/(length*notesPerSecond))
      sound = makeEmptySound(totalSamples, rate)
      SAMPS = getSamples(sound)
      PIXS = getPixels(picture)
      ## This is where the sound starts (sample 0)
      lastIndex = 0
      lastPixelIndex = 0
      noteLow = requestIntegerInRange("Please give a number between 1 and 88,\n"+
                                       "which is the lowest key number\n(recommend 32)", 1, 88)
      noteHigh = requestIntegerInRange("Please give a number between "+str(noteLow)+" and 88,\n"+
                                        "which is the highest key number\n(recommend 64)", noteLow, 88)
      ## This part is calculating the frequencies of the piano keys based on the key number (1 is low, 88 is high)
      daNotes = {}
      for i in range(1,89):
         base = pow(2, (1.0/12))
         power = i-49
         freq = pow(base, power) * 440.0
         daNotes[i] = freq
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
         #END FOR
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
         #END FOR
         lastIndex += (x*sampsPerWave)
      writeSoundTo(sound, self.currentDirectory + "/" + file_name.split(".")[0] + "_sound.wav")
   #END DEF
   
   
   # DESC: This converts a given .wav file into a visualization of the waveform 
   #       (exported as a video file)
   #
   # INPUTS:   wav file
   # OUTPUTS:  avi file (and potentially a series of jpg images)
   def Peter_Second_Project(self, event=""):
      import random
      import string   ## USED TO GET FILE NAME
      import shutil   ## USED TO COPY AND DELETE IMAGES FOLDER
      #Getting the file chosen
      selected = self.files.getSelectedIndices()
      selectedFile = self.files.getModel( ).getElementAt( selected[0])
      selectedFile = self.currentDirectory + "/"+ selectedFile
      file_name = selectedFile[selectedFile.rfind("/")+1:]
      #Checking that the file is a wav file
      fileExt = file_name.split(".")[-1]
      if (fileExt not in self.soundExts):
         mywindow = swing.JFrame(size=(600,100))
         mywindow.contentPane.layout = java.awt.FlowLayout(java.awt.FlowLayout.CENTER)
         mywindow.contentPane.add(swing.JLabel(file_name+" is not a wav file"))
         mywindow.setLocationByPlatform(true)
         mywindow.visible = true
         return None
      continueThis = requestString("This function can take a while to run.\n" + 
                                    "Assume about 1.5 minutes of processing per 1 minute of audio.\n" + 
                                    "Continue? (y/n)")
      if continueThis != "y":
         return None
      # --------------------
      folder = "/visualizer_images/"
      #This creates the folder at the specified location above
      # If the folder is already created, it will first delete it, then create it again
      try:
         os.makedirs(self.currentDirectory + folder)
      except OSError:
         shutil.rmtree(self.currentDirectory + folder)
         os.makedirs(self.currentDirectory + folder)
      #Getting some basic information about the sound
      SOUND = makeSound(selectedFile)
      rate = getSamplingRate(SOUND)
      SAMPLES = getSamples(SOUND)
      numSamples = getNumSamples(SOUND)
      #Declaring necessary numbers for loops and index counters
      framesPerSec = 25
      sampleSectionsPerFrame = 40
      lastSecondSectionCount = int( sampleSectionsPerFrame*(float(5)/8) )
      nextHalfSecondSectionCount = int( sampleSectionsPerFrame*(float(3)/8) )
      #This is also how many pixels there will be per section
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
      #END FOR
      #This will be multiplied into the sample value to give
      # the vertical amount that will be added to our line
      ratio = float(height/2)/maxSampValue
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
      while sampleIndex < ( numSamples+(samplesPerSection*(pixelsPerSection*nextHalfSecondSectionCount)) ):
         picture = makeEmptyPicture(width, height, black)
         soundColor = white
         lineColor = red
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
            #END FOR
            sampleIndex += samplesPerSection
            newAverages[q] = int( (float(sampleAvg)/samplesPerSection) )
         #END FOR
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
            #END FOR
         #END FOR
         #Iterate frame index before saving picture
         frameIndex += 1
         #This section is for naming the picture, and padding the appropiate number of 0's
         if frameIndex<10:
            writePictureTo(picture, self.currentDirectory + folder + "frame0000" + str(frameIndex) + ".jpg")
         elif frameIndex<100:
            writePictureTo(picture, self.currentDirectory + folder + "frame000" + str(frameIndex) + ".jpg")
         elif frameIndex<1000:
            writePictureTo(picture, self.currentDirectory + folder + "frame00" + str(frameIndex) + ".jpg")  
         elif frameIndex<10000:
            writePictureTo(picture, self.currentDirectory + folder + "frame0" + str(frameIndex) + ".jpg")
         else:
            writePictureTo(picture, self.currentDirectory + folder + "frame" + str(frameIndex) + ".jpg")
      #END WHILE
      #This is where the movie is created
      mov = makeMovieFromInitialFile(self.currentDirectory + folder + "frame00001.jpg")
      writeAVI(mov, self.currentDirectory + "/" + file_name[:-4] + ".avi", framesPerSec)
      response = requestString("Would you like to keep the folder of images? (y/n) ")
      while (response != "y") and (response != "n"):
         response = requestString("Would you like to keep the folder of images? (y/n) ")
      if response == 'n':
         try:
            shutil.rmtree(self.currentDirectory+folder)
         except OSError:
            deleted = false
      #END IF
      return None
   #END DEF
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# THESE ARE THE PICTURE FILTERS
   # DESC: This converts the image into a very contrasting, black and white image. Using an algorithm,
   #       pixels are turned either solid black or white. The resulting image is then displayed
   #
   # INPUTS:   none
   # OUTPUTS:  none
   def BlackAndWhite(self, event=""):
      self.newpicture = makePicture(self.currentPicturePath)
      for px in getPixels(self.newpicture):
         rcolor = getRed(px)
         gcolor = getGreen(px)
         bcolor = getBlue(px)
         average = (rcolor+gcolor+bcolor)/3
         if (average > 128):
            setColor(px, black)
         elif (average <=128):
            setColor(px, white)
         #END IF/ELIF
      #END FOR
      self.refresh()
      return true
   #END DEF
   
   
   # DESC: ..
   #
   # INPUTS:   none
   # OUTPUTS:  none
   def grayscale(self, event=""):
      self.newpicture = makePicture(self.currentPicturePath)
      for px in getPixels(self.newpicture):
         level = 255 - int(0.21*getRed(px) + 0.71*getGreen(px) +0.07*getBlue(px))
         color = makeColor(level, level, level)
         setColor(px, color)
      #END FOR
      self.refresh()
      return true
   #END DEF
   
   
   # DESC: This asks the user what two colors in the image they would like swapped.
   #       The program swaps the RGB values of the colors they chose, and displays the end image
   #
   # INPUTS:   2 String, the colors the user wishes to swap
   # OUTPUTS:  none
   def redGreenBlueSwap(self, event=""):
      import string as str
      self.newpicture = makePicture(self.currentPicturePath)
      color1 = str.lower(requestString("Enter Red, Blue or Green"))
      color2 = str.lower(requestString("Enter Red, Blue or Green"))
      check = ['red', 'blue', 'green']
      if (color1 not in check or color2 not in check):
        return none
      #
      # Here ask the user what colors they want to swap
      #
      #self.testing(text=color1)
      for px in getPixels(self.newpicture):
        value=px
        
        if (color1=="red" and color2=="blue"):
          rcolor = getRed(px)
          bcolor = getBlue(px)
          setRed(px, bcolor)
          setBlue(px, rcolor)
          
        elif (color1=="red" and color2=="green"):
          rcolor = getRed(px)
          gcolor = getGreen(px)
          setRed(px, gcolor)
          setGreen(px, rcolor)
          
        elif (color1=="green" and color2=="blue"):
          gcolor = getGreen(px)
          bcolor = getBlue(px)
          setGreen(px, bcolor)
          setBlue(px, gcolor)
          
        elif (color1=="green" and color2=="red"):
          gcolor = getGreen(px)
          rcolor = getRed(px)
          setGreen(px, rcolor)
          setRed(px, gcolor)
          
        elif (color1=="blue" and color2=="green"):
          bcolor = getBlue(px)
          gcolor = getGreen(px)
          setBlue(px, gcolor)
          setGreen(px, bcolor)
          
        elif (color1=="blue" and color2=="red"):
          bcolor = getBlue(px)
          rcolor = getRed(px)
          setBlue(px, rcolor)
          setRed(px, bcolor)
        
          
      #END FOR
      #self.testing(text="BLAH")
      self.refresh()
      return true
   #END DEF   
   
   # DESC: This makes a negative of the orignal image (for each pixel value, reassign
   #       as 255 - value)
   #
   # INPUTS:   none
   # OUTPUTS:  none
   def negativeFlip(self, event=""):
      self.newpicture = makePicture(self.currentPicturePath)
      for px in getPixels(self.newpicture):
         a_red=getRed(px)
         a_green=getGreen(px)
         a_blue=getBlue(px)
         negColor=makeColor(255 - a_red, 255 - a_green, 255 - a_blue)
         setColor(px, negColor)
      #END FOR
      self.refresh()
      return true
   #END DEF
   
   
   # DESC: This removes all but the specified color from the image
   #
   # INPUTS:   String, color
   # OUTPUTS:  none
   def singleColorScale(self, event=""):
      self.newpicture = makePicture(self.currentPicturePath)
      color_string = str.lower(requestString("Enter Red, Blue or Green"))
      for px in getPixels(self.newpicture):
         a_red = 0
         a_green = 0
         a_blue = 0
         if color_string == "red":
            a_red = getRed(px)
         elif color_string == "green":
            a_green = getGreen(px)
         elif color_string == "blue":
            a_blue = getBlue(px)
         else:
            a_red = getRed(px)
         #END IF/ELIF/ELSE
         newcolor = makeColor(a_red, a_green, a_blue)
         setColor(px, newcolor)
      #END FOR
      self.refresh()
      return true
   #END DEF
   
   
   # DESC: Pixelizes the image, so that the image is a little more grainy
   #
   # INPUTS:   Integer, the scale of graininess (i.e. the number of pixels that will be combined)
   # OUTPUTS:  none
   def pixelizeME(self, event=""):
      self.newpicture = makePicture(self.currentPicturePath)
      pixelization = requestIntegerInRange("Please specify the scale of pixelization (2-10)", 2, 10)
      height = getHeight(self.newpicture)
      width = getWidth(self.newpicture)
      for rrow in range(0, height, pixelization):
         for rcol in range(0, width, pixelization):
            ttlRed = 0
            ttlGreen = 0
            ttlBlue = 0
            ttlPixelCount = 0
            for row in range(rrow, min(rrow + pixelization, height)):
               for col in range(rcol, min(rcol + pixelization, width)):
                  pixel = getPixel(self.newpicture, col, row)
                  ttlRed += getRed(pixel)
                  ttlGreen += getGreen(pixel)
                  ttlBlue += getBlue(pixel)
                  ttlPixelCount += 1
                #END FOR
            #END FOR
            avgRed = ttlRed / ttlPixelCount
            avgGreen = ttlGreen / ttlPixelCount
            avgBlue = ttlBlue / ttlPixelCount
            for row in range(rrow, min(rrow + pixelization, height)):
               for col in range(rcol, min(rcol + pixelization, width)):
                  pixel = getPixel(self.newpicture, col, row)
                  pixel.setRed(avgRed)
                  pixel.setGreen(avgGreen)
                  pixel.setBlue(avgBlue)
               #END FOR
            #END FOR
         #END FOR
      #END FOR
      self.refresh()
      return true
   #END DEF
   
   
   # DESC: Copies the half of the image specified along the given axis.
   #       Axes are based off of the center of the photo (imagine drawing a line down or across the center)
   #
   # INPUTS:   axis, String (x or y)
   #           half, String (up, down, left, or right)
   # OUTPUTS:  none
   def mirrorOnAxis(self, event=""):
      self.newpicture = makePicture(self.currentPicturePath)
      axis = str.lower(requestString("Please specify the center axis you would like the image mirrored on (X, or Y)"))
      half = str.lower(requestString("Please specify which half you would like to keep.\nUp or Down (for X axis), Left or Right (for Y axis)"))
      height = getHeight(self.newpicture)
      width = getWidth(self.newpicture)
      if axis == "x" or axis != "y":
         if half == "up" or half != "down":
            start = height/2
            end = height
         else:
            start = 0
            end = height/2
            height -= 1
         #END IF/ELSE
         for row in range(start, end):
            for col in range(0, width):
               pixelOrig = getPixel(self.newpicture, col, (height-row)).getColor()
               pixelMirror = getPixel(self.newpicture, col, row)
               pixelMirror.setColor(pixelOrig)
            #END FOR
         #END FOR
      else:
         if half == "left" or half != "right":
            start = width/2
            end = width
         else:
            start = 0
            end = width/2
            width -= 1
         #END IF/ELSE
         for row in range(0, height):
            for col in range(start, end):
               pixelOrig = getPixel(self.newpicture, (width-col), row).getColor()
               pixelMirror = getPixel(self.newpicture, col, row)
               pixelMirror.setColor(pixelOrig)
            #END FOR
         #END FOR
      #END IF/ELSE
      self.refresh()
      return true
   #END DEF
   
#END CLASS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #












# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MAIN
import time
printNow("Please use this GUI to run some of our previous projects")
time.sleep(1)
fcv = FileContentsViewer()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
