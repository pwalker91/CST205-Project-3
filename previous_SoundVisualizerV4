# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# This is the line object.
# It has a start point (x,y), an end point (x,y), and a color.
# By default, these are (0,0), (1,1), and white
# Slope is the integer representing the rise over run of the two points
# Slope angle is the angle made between the line and the x-axis (in radians)
class Line(object):
   # This is the initializer, which is run every time a Line object is created
   # The first section of IFs checks to see that the given points are made of integers
   def __init__(self, startX=0, startY=0, endX=1, endY=1, myColor=white):
      if not(isinstance(startX, int)):
         raise TypeError("StartX was not an int. Was given "+type(startX))
      if not(isinstance(startY, int)):
         raise TypeError("StartY was not an int. Was given "+type(startY))
      if not(isinstance(endX, int)):
         raise TypeError("EndX was not an int. Was given "+type(endX))
      if not(isinstance(endY, int)):
         raise TypeError("EndY was not an int. Was given "+type(endY))
      if myColor.__class__.__name__ != "Color":
         raise TypeError("You did not pass in a Color object.")
      self.startX = startX
      self.startY = startY
      self.endX = endX
      self.endY = endY
      self.myColor = myColor
      self.calcSlope()
   ##END DEF
   
   #This is the method called when you use str(self). Prints out the variables
   def __str__(self):
      return ( "Start:"+str(self.startX)+","
                       +str(self.startY)+
              "-End:"+str(self.endX)+","
                     +str(self.endY)+
              "-m:"+str(self.slope)+"(ratio),"
                   +str(self.slopeAngle)+"(radians)"
              "-Color:"+str(self.myColor.getRed())+","
                         +str(self.myColor.getGreen())+","
                         +str(self.myColor.getBlue()) )
   ##END DEF
   
   #These are the getters and setters for the start and end points of the line
   def setStartX(self, x):
      self.startX = x
      self.calcSlope()
   ##END DEF
   def setStartY(self, y):
      self.startY = y
      self.calcSlope()
   ##END DEF
   def getStartX(self):
      return self.startX
   ##END DEF
   def getStartY(self):
      return self.startY
   ##END DEF
   
   def setEndX(self, x):
      self.endX = x
      self.calcSlope()
   ##END DEF
   def setEndY(self, y):
      self.endY = y
      self.calcSlope()
   ##END DEF
   def getEndX(self):
      return self.endX
   ##END DEF
   def getEndY(self):
      return self.endY
   ##END DEF
   
   #These functions calculate the slope or slope angle values, given the points, the slope
   # or the slope angle
   def calcSlope(self):
      try:
         self.slope = float(self.endY-self.startY)/(self.endX-self.startX)
         self.slopeAngle = atan(self.slope)
      except ZeroDivisionError:
         self.slopeAngle = pi/2
   ##END DEF
   def calcSlopeAngle(self):
      self.slopeAngle = atan(self.slope)
   ##END DEF
   def calcSlopeFromAngle(self):
      self.slope = tan(self.slopeAngle)
   ##END DEF
   
   #Setting and getting the color
   def setMyColor(self, color):
      if color.__class__.__name__ == "Color":
         self.myColor = color
         return "Line Color was changed to ~"+str(color)+"~"
      else:
         raise TypeError("You did not pass in a Color object.")
   ##END DEF
   def getMyColor(self):
      return self.myColor
   ##END DEF
   
   #Drawing the line on the given picture object
   def drawLine(self, picture):
      if picture.__class__.__name__ == "Picture":
         picture.addLine(self.myColor, self.startX, self.startY, self.endX, self.endY)
      else:
         raise TypeError("You did not pass in a Picture object.")
   ##END DEF
##END CLASS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# This is the Limb object
# It has a line attribute and a branches attribute
# The line is a Line object, and the branches attribute is an array of branches
# The hasBranches attribute is for determining whether the object has branches or not
class Limb(object):
   #The object on creation must be pass a Line object, a level,
   # and optionally a boolean on whether the object has Branches or not
   def __init__(self, line, level=0, hasBranches=false):
      if line.__class__.__name__ == "Line":
         self.line = line
         self.level = level
      else:
         raise TypeError("You did not pass in a Line object")
      self.hasBranches = hasBranches
      if self.hasBranches:
         self.branches = []
   ##END DEF
   #Printing out the Limb object
   def __str__(self):
      returnable = "|Limb:"+str(self.line)+"|"
      if self.hasBranches:
         for branch in self.branches:
            returnable += str(branch)
      return returnable
   ##END DEF
   
   #Getter and setter for the Line attribute
   def getLine(self):
      return self.line
   ##END DEF
   def setLine(self, line):
      if line.__class__.__name__ == "Line":
         self.line = line
      else:
         raise TypeError("You did not pass in a Line object.")
   ##END DEF
   
   #Methods for adding, removing, and getting all of the Branches in the object
   def addBranch(self, branch):
      if self.hasBranches:
         if branch.__class__.__name__ == "Branch":
            self.branches.append(branch)
            return len(self.branches)-1
         else:
            raise TypeError("You did not pass in a Line object.")
      else:
         raise StandardError("You cannot call this function for this object. This limb has no Branches")
   ##END DEF
   def removeBranch(self, index):
      if self.hasBranches:
         if (index >= len(self.branches)) or (index < 0):
            raise IndexError("You did not pass a correct index. It must be between 0 and "+str(self.size))
         else:
            return self.branches.pop(index)
      else:
         raise StandardError("You cannot call this function for this object. This limb has no Branches")
   ##END DEF
   def getBranch(self, index):
      if self.hasBranches:
         if (index >= len(self.branches)) or (index < 0):
            raise IndexError("You did not pass a correct index. It must be between 0 and "+str(self.size))
         else:
            return self.branches[index]
      else:
         raise StandarError("You cannot call this function for this object. This limb has no Branches")
   ##END DEF
   def getAllBranches(self):
      if self.hasBranches:
         return self.branches
      else:
         raise StandardError("You cannot call this function for this object. This limb has no Branches")
   ##END DEF
   
   #Draws the limb based on the Line attribute, and draws any subsequent branches
   def drawLimb(self, picture):
      self.line.drawLine(picture)
      #This was going to save rather than repaint
      repaint(picture)
      #
      if self.hasBranches:
         for branch in self.branches:
            branch.drawAllLimbs(picture)
   ##END DEF
##END CLASS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# This is the branch object.
# It has a size (number of limbs) and an array of Limbs
# Initially, the size is 0 and the array is empty
class Branch(object):
   def __init__(self, level):
      self.size = 0
      self.limbs = []
      self.level = level
   ##END DEF
   def __str__(self):
      returnable = ""
      spacing = ""
      for i in range(0,self.level):
         spacing += "  ~~  "
      
      if len(self.limbs)==0:
         return "Branch has no limbs"
      for limb in self.limbs:
         returnable += "\n"+spacing+str(limb)
      return returnable
   ##END DEF
   
   #These methods add, remove, and get the Limbs in the branch object
   def addLimb(self, limb):
      if limb.__class__.__name__ == "Limb":
         self.limbs.append(limb)
         self.size+=1
         return self.size
      else:
         raise TypeError("You did not pass in a Limb object.")
   ##END DEF
   def removeLimb(self, index):
      if (index >= self.size) or (index < 0):
         raise IndexError("You did not pass a correct index. It must be between 0 and "+str(self.size))
      else:
         self.size-=1
         return self.limbs.pop(index)
   ##END DEF
   def getLimb(self, index):
      if (index >= self.size) or (index < 0):
         raise IndexError("You did not pass a correct index. It must be between 0 and "+str(self.size))
      else:
         return self.limbs[index]
   ##END DEF
   def getAllLimbs(self):
      return self.limbs
   ##END DEF
   
   #Draws all limbs in the object on the given picture
   def drawAllLimbs(self, picture):
      for limb in self.limbs:
         limb.drawLimb(picture)
   ##END DEF
##END CLASS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 







# Takes a given array of sample values, a number of section to split it into, and a multiplier
# for the averager.
## The array given will be split into X number of sections, and each section will averages all
## of the sample values. These values are then added to an array (which will be returned).
## Before returning the array, the values are reduced to values between about -1 and 1, because
## these values are later added to a radian measurement.
def averagesForSampleSections(soundArray, numSections, multiplier):
   # Checks to make sure that an array was passed through
   if soundArray.__class__.__name__ != "array":
      raise TypeError("You did not pass in an array. Are you passing in the Sound object? Or the array of Sample Objects?")
   if isinstance(numSections, int) and (numSections<1):
      raise StandarError("The number of sections must be an integer greater than 0")
   
   # If the number of section is not one, it recursively runs the function with a slice of the original array
   # If the number is one, the values are averaged and returned to the IF above
   averages = []
   if numSections != 1:
      sectionLength = len(soundArray)/numSections
      for i in range(0,numSections):
         averages.append( averagesForSampleSections(soundArray[(i*sectionLength):((i+1)*sectionLength)], 1, 1) )
   else:
      total = 0
      for i in range(0, len(soundArray)):
         total += float(soundArray[i].value)
      return total/(len(soundArray))
   
   # This part makes the values in the returned array more useable to the other functions
   angleMin = min(averages)
   angleMax = max(averages)
   dist = angleMax-angleMin
   for i in range(0, len(averages)):
      averages[i] = averages[i]/(dist*multiplier)
   return averages
##END DEF


# This function takes a given branch of limbs, a starting and ending point (as 4 integers),
# the average length the whole branch should cover (in number of pixels) and an array of radian values.
## The function will create as many limbs as there are arrays in the sectionArray
## The sectionArray is structured such ( [2.34, 7.992, 0.0198, .....] )
## Once the function figures out how many "Limbs" there will be, it creates their Lines, whose direction
## is starting at the previous Line's end and ending towards the end point. However, the slope of the line (the angle)
## has a random value added, which is the value in sectionArray at the same index
def calculateLimbs(branch, thisStartX,thisStartY, thisEndX,thisEndY, branchDist, sectionArray):
   import random
   if branch.__class__.__name__ != "Branch":
      raise TypeError("You did not pass in a Branch object")
   if (sectionArray.__class__.__name__ != "array") and (sectionArray.__class__.__name__ != "list"):
      raise TypeError("You did not pass in an array object")
   if not( isinstance(thisStartX, int) and isinstance(thisStartY, int)
           and isinstance(thisEndX, int) and isinstance(thisEndY, int) ):
      raise TypeError("Your given points were not made of integers")
   
   #Each limb is going to be as long as the whole distance (given value) divided by the number of limbs
   limbLength = branchDist/(len(sectionArray))
   random.seed(sum(sectionArray))
   
   #This for loop will create as many limbs as there are values in the section array
   for k in range(0, len(sectionArray)):
      color = makeColor(random.randint(30,255),random.randint(30,255),random.randint(30,255))
      #The start Y and end Y are always known, because the Y increases the same amount
      limb = Limb( Line( startY=(thisStartY+(k*limbLength)),
                         endY=(thisStartY+((k+1)*limbLength)),
                         myColor=color),
                   branch.level, true )
      #If this is the first limb, use the given start X, otherwise, use the last limb's end X
      if k==0:
         limb.line.setStartX(thisStartX)
      else:
         limb.line.setStartX(branch.getLimb(k-1).line.endX)
      
      #Try finding the angle of the slope between the current limb's start X and Y and the
      # overall end X and Y. If the slope is vertical, the slope is infinity, and so we set
      # the angle to be pi/2
      try:
         slopeToTempEnd = (thisEndY-limb.line.startY) / (thisEndX-limb.line.startX)
         angleToTempEnd = atan(slopeToTempEnd)
      except ZeroDivisionError:
         angleToTempEnd = (pi/2)
      
      #Adding the random radian amount to the angle
      limb.line.slopeAngle = angleToTempEnd+sectionArray[k]
      
      #Calculating the end X value based on the start X, slope, and change in Y
      if (thisStartX<thisEndX):
         limb.line.setEndX( limb.line.startX + int(limbLength * cos(limb.line.slopeAngle)) )
      else:
         limb.line.setEndX( limb.line.startX - int(limbLength * cos(limb.line.slopeAngle)) )
      #
      printNow(str(limb.line))
      #
      branch.addLimb(limb)
##END DEF













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
   
   width = 600
   height = 700
   picture = makeEmptyPicture(width, height, black)
   
   SAMPLES = getSamples(SOUND)
   numSamples = getNumSamples(SOUND)
   
   
   #
   # DRAWING THE MAIN BRANCH
   #
   numMainBranchLimbs = 6
   numSubBranches = 3
   numSubBranchLimbs = 5
   numSubSubBranches = 14
   
   mainBranchLength = int( height*(float(7)/8) )
   subBranchLength = int( (width/2)*(float(2)/3) )
   subSubBranchLength = int( subBranchLength*0.3)
   
   branchStartX = picture.getWidth()/2
   branchStartY = 0
   branchEndX = picture.getWidth()/2
   branchEndY = mainBranchLength
   
   mainBranch = Branch(0)
   calculateLimbs(mainBranch,
                  int(branchStartX),int(branchStartY),
                  int(branchEndX),int(branchEndY),
                  mainBranchLength,
                  averagesForSampleSections(SAMPLES, numMainBranchLimbs, 1))
   
   #printNow(averagesForSampleSections(SAMPLES, numMainBranchLimbs))
   ""
   mainBranch.drawAllLimbs(picture)
   writePictureTo(picture, desktop+"temp_01.jpg")
   ""
   
   #
   # DRAWING THE FIRST SUB BRANCHES
   #
   sectionedSAMPLES = []
   sectionedLength = len(SAMPLES)/numMainBranchLimbs
   for k in range(0, numMainBranchLimbs):
      sectionedSAMPLES.append(SAMPLES[(k*sectionedLength):((k+1)*sectionedLength)])
   
   TEMPCOUNT = 0
   for limb in mainBranch.limbs:
      TEMPCOUNT+=1
      thisLimbHeight = limb.line.endY-limb.line.startY
      thisLimbSectionHeight = thisLimbHeight/numSubBranches
      
      subLimbInverseSlope = -1.0/limb.line.slope
      subBranchXDelta = subBranchLength * cos(tan(subLimbInverseSlope))
      
      for k in range(0, numSubBranches):
         
         subBranchStartY = limb.line.startY + (k*thisLimbSectionHeight)
         subBranchStartX = ( ((subBranchStartY-limb.line.startY)
                              +(limb.line.slope*limb.line.startX))
                                 /limb.line.slope)
         if (k%2)==0:
            subBranchEndX = subBranchStartX + subBranchXDelta
         else:
            subBranchEndX = subBranchStartX - subBranchXDelta
         subBranchEndY = (subLimbInverseSlope*(subBranchEndX-subBranchStartX))+subBranchStartY
         limb.addBranch(Branch(limb.level+1))
         
         """
         if k>2 and false:
            sys.exit()
         else:
            printNow("subBranch "+str(TEMPCOUNT)+" "+str(k+1))
            printNow(str(subBranchStartX)+" "+str(subBranchStartY)+" "+str(subBranchEndX)+" "+str(subBranchEndY))
            printNow("")
         """
         
         calculateLimbs(limb.getBranch(k),
                        int(subBranchStartX),int(subBranchStartY),
                        int(subBranchEndX),int(subBranchEndY),
                        subBranchLength,
                        averagesForSampleSections(sectionedSAMPLES[k], numSubBranchLimbs, numSubBranchLimbs))
         limb.drawLimb(picture)
         writePictureTo(picture, desktop+"temp_"+str(TEMPCOUNT)+str(k)+".jpg")
      ##END FOR
   ##END FOR
   
   #
   # Redraw all branches
   #
   ""
   mainBranch.drawAllLimbs(picture)
   writePictureTo(picture, desktop+"temp_02.jpg")
   printNow(str(mainBranch))
   ""
         
         
      
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   ###
   
   ## THIS PART BELOW IS FROM THE PREVIOUS ITERATION, AND WAS GOING TO BE USED AS A TEMPLATE FOR
   ## THE FINISHED FUNCTION
   
   ###
   
   
   
   
   
   
   
   
   """
   
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
   while sampleIndex<numSamples+(samplesPerSection*nextHalfSecondSectionCount):
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
      
      #printNow(averagesArray)
      
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
   """
   """
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
   """








