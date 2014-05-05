import javax.swing as swing
import os, os.path
import java

fd=r"C:\\Users\\Pilot\\My Documents\\GitHub\\CST205-Project-3"

printNow(os.path.isdir(fd))

os.chdir(fd)

printNow(os.getcwd())

class FileContentsViewer(swing.JFrame):
  def __init__(self):
    swing.JFrame.__init__(self, title="File Contents Viewer", size=(200,200))
    self.contentPane.layout=java.awt.FlowLayout()
    
    self.field=swing.JTextField(size=(200,60))
    self.field.text="barbara.jpg"
    self.contentPane.add(self.field)
    
    fileView = swing.JButton("View Contents", size=(65,30), actionPerformed=self.checkContents)
    self.contentPane.add(fileView)
    
    setFolder = swing.JButton("Set Folder", size=(65,30), actionPerformed=self.setFolder)
    self.contentPane.add(setFolder)
    
    self.visible=1
    
  def checkContents(self,event):
    if self.field.text.endswith(".jpg"):
      pic = makePicture(getMediaPath(self.field.text))
      show(pic)
    if self.field.text.endswith(".wav"):
      snd=makeSound(getMediaPath(self.field.text))
      play(snd)
  
  def setFolder(self,event):
    setMediaPath()

class FileContentsViewer2(swing.JFrame):
  def __init__(self,directory):
    swing.JFrame.__init__(self, title="File Contents Viewer", size=(210,250))
    self.contentPane.layout = java.awt.BorderLayout()
    
    self.currentDirectory = directory
    self.files=swing.JList(os.listdir(self.currentDirectory))
    pane = swing.JScrollPane(self.files)
    self.contentPane.add(pane,java.awt.BorderLayout.CENTER)
    
    fileView = swing.JButton("View Contents", size=(65,30), actionPerformed=self.fileView)
    self.contentPane.add(fileView, java.awt.BorderLayout.SOUTH)
    self.pack()
    self.visible=1
    
  def fileView(self,event):
    selected=self.files.getSelectedIndices()
    selectedFile = self.files.getModel().getElementAt(selected[0])
    selectedFile = self.currentDirectory+"//"+selectedFile
    if selectedFile.endswith(".jpg"):
      pic = makePicture(selectedFile)
      show(pic)
    if selectedFile.endswith(".wav"):
      snd = makeSound(selectedFile)
      play(snd)
      
class FileContentsViewer3(swing.JFrame):
  def __init__(self,directory=""):
    swing.JFrame.__init__(self, title="File Contents Viewer", size=(210,250))
    self.contentPane.layout = java.awt.BorderLayout()
    
    self.currentDirectory=setMediaPath()
    
    directoryList = os.listdir(self.currentDirectory)
    
    self.files=swing.JList(directoryList)
    pane = swing.JScrollPane(self.files)
    self.contentPane.add(pane,java.awt.BorderLayout.CENTER)
    
    fileView = swing.JButton("View Contents", size=(65,30), actionPerformed=self.fileView)
    self.contentPane.add(fileView, java.awt.BorderLayout.EAST)
    
    changeDir = swing.JButton("Change Directory", size=(65,30), actionPerformed=self.changeDirectory)
    self.contentPane.add(changeDir, java.awt.BorderLayout.SOUTH)
    print "here"
    
    self.pack()
    self.visible=1
    
  def fileView(self,event):
    selected=self.files.getSelectedIndices()
    selectedFile = self.files.getModel().getElementAt(selected[0])
    selectedFile = self.currentDirectory+"//"+selectedFile
    if selectedFile.endswith(".jpg"):
      pic = makePicture(selectedFile)
      show(pic)
      del selected
      del selectedFile
    if selectedFile.endswith(".wav"):
      snd = makeSound(selectedFile)
      play(snd)
    
  def changeDirectory(self, event):
    self.contentPane.removeAll()
    self.currentDirectory=setMediaPath()
    directoryList = os.listdir(self.currentDirectory)
    self.files=swing.JList(directoryList)
    pane = swing.JScrollPane(self.files)
    self.contentPane.add(pane, java.awt.BorderLayout.CENTER)
    fileView = swing.JButton("View Contents", size=(65,30), actionPerformed=self.fileView)
    self.contentPane.add(fileView, java.awt.BorderLayout.EAST)
    changeDir = swing.JButton("Change Directory", size=(65,30), actionPerformed = self.changeDirectory)
    self.contentPane.add(changeDir, java.awt.BorderLayout.SOUTH)
    self.pack()
    self.visible = true