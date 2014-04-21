import javax.swing as swing
import os
import java

class FileRunner(swing.JFrame):
  def __init__(self):
    swing.JFrame.__init__(self, title="File Runner", size=(250,250))
    self.contentPane.layout = java.awt.BorderLayout()
    
    files = []
    
    self.currentDirectory = "C:\\Users\\Pilot\\My Documents\\CST 205\\"
    self.files = swing.JList(os.listdir(self.currentDirectory))
    pane = swing.JScrollPane(self.files)
    self.contentPane.add(pane,java.awt.BorderLayout.CENTER)
    
    fileView = swing.JButton("View Contents", size=(65,30),
    actionPerformed=self.fileView)
    self.contentPane.add(fileView, java.awt.BorderLayout.SOUTH)
    
    first = swing.JButton("Speed Up Audio", size=(65,30),actionPerformed=self.first)
    self.contentPane.add(first, java.awt.BorderLayout.WEST)
    
    second = swing.JButton("Create Audio Video", size=(65,30),actionPerformed=self.second)
    self.contentPane.add(second, java.awt.BorderLayout.EAST)
    
    self.pack()
    self.visible = 1
    
  def fileView(self,event):
    print "Hello!"
    selected=self.files.getSelectedIndices()
    selectedFile = self.files.getModel( ).getElementAt( selected[0])
    selectedFile = self.currentDirectory+ "//"+ selectedFile
    if selectedFile.endswith(".jpg"):
      pic = makePicture(selectedFile)
      show(pic)
    if selectedFile.endswith(".wav"):
      snd = makeSound
  
  def first(self, event):
    dir='C:\\Users\\Pilot\\My Documents\\CST 205\\pictures\\'
    if not os.path.exists(dir):
      os.makedirs(dir)
    x=0
    y=0
    value=0
    data = requestInteger("Please enter a picture size: ")
    picture=makeEmptyPicture(data,data)
    file=pickAFile()
    sound=makeSound(file)
    overall=(getNumSamples(sound))/(data*data)
    int(overall)
    pixelArray=getPixels(picture)
    pixelIndex=0
    for k in range (0, data):
      for i in range (0, data):
        total=0
        for j in range (0, overall):
          total+=getSampleValueAt(sound, ((k*overall*data)+(i*overall)+j))
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
        pixelIndex+=1
      value=value+1
      if(value<10):
        writePictureTo(picture, dir+'photo000'+str(value)+'.jpg')
      elif(value<100):
        writePictureTo(picture, dir+'photo00'+str(value)+'.jpg')
      elif(value<1000):
        writePictureTo(picture, dir+'photo0'+str(value)+'.jpg')
      else:
        writePictureTo(picture, dir+'photo'+str(value)+'.jpg')
    show(picture)
    mov = makeMovieFromInitialFile(pickAFile())
    writeAVI(mov, dir+'newMovie.avi', 20)
  
  def second(self, event):
    s = pickAFile()
    sound = makeSound(s)
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
