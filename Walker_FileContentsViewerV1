# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Java Swing GUI class
class FileContentsViewer(swing.JFrame):

   #Initialization function for the FileContentsViewer object
   def __init__(self):
      swing.JFrame.__init__(self, title="File Contents Viewer", size=(200,200))
      self.contentPane.layout = java.awt.FlowLayout()
      
      self.field = swing.JTextField(size=(200,60))
      self.field.text = "barbara.jpg"
      self.contentPane.add(self.field)
      
      fileView = swing.JButton("View Contents", size=(65,30),
                               actionPerformed=self.checkContents)
      self.contentPane.add(fileView)
      
      setFolder = swing.JButton("Set Folder", size=(65,30),
                                actionPerformed=self.setFolder)
      self.contentPane.add(setFolder)
      self.visible = 1
   # END DEF
   
   def checkContents(self,event):
      if self.field.text.endswith(".jpg"):
         pic = makePicture(getMediaPath(self.field.text))
      show(pic)
      if self.field.text.endswith(".wav"):
         snd=makeSound(getMediaPath(self.field.text))
      play(snd)
      if raw_input("Press enter to stop"):
         stopPlaying(snd)
   # END DEF
   
   def setFolder(self,event):
      setMediaPath()
   # END DEF
   
# END CLASS


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MAIN
printNow("Creating a File Contents Viewer")
fcv = FileContentsViewer()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #