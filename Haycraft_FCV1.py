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
    self.message.text = "Hello!"
  
  def second(event):
    printNow("DUH!")