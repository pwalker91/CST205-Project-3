
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Scrollable File Contents Viewer class
class FileContentsViewer(swing.JFrame):
   import os
   import java
   def __init__(self, directory=""):
      swing.JFrame.__init__(self, title="File Contents Viewer", size=(500,350))
      self.contentPane.layout = java.awt.BorderLayout()
      
      filesList = self.listFilesInDirectory(directory)
      
      self.files = swing.JList(filesList)
      pane = swing.JScrollPane(self.files)
      self.contentPane.add(pane, java.awt.BorderLayout.CENTER)
      
      
      ""
      fileView = swing.JButton("View Contents", size=(65,30),
                               actionPerformed = self.fileView)
      self.contentPane.add(fileView, java.awt.BorderLayout.WEST)
      ""
      changeDir = swing.JButton("Change Directory", size=(65,30),
                               actionPerformed = self.changeDirectory)
      self.contentPane.add(changeDir, java.awt.BorderLayout.SOUTH)
      ""
      smallFrame = swing.JPanel(java.awt.GridLayout(0,1))
      smallFrame.add(swing.JButton("1", actionPerformed=self.testing))
      smallFrame.add(swing.JButton("2", actionPerformed=self.testing))
      smallFrame.add(swing.JButton("3", actionPerformed=self.testing))
      smallFrame.add(swing.JButton("3", actionPerformed=self.testing))
      smallFrame.add(swing.JButton("3", actionPerformed=self.testing))
      smallFrame.add(swing.JButton("3", actionPerformed=self.testing))
      self.contentPane.add(smallFrame, java.awt.BorderLayout.EAST)
      
      self.pack()
      self.visible = true
   #END DEF
   
   def fileView(self, event):
      selected = self.files.getSelectedIndices()
      selectedFile = self.files.getModel( ).getElementAt( selected[0])
      selectedFile = self.currentDirectory+ "/"+ selectedFile
      if (selectedFile.endswith(".jpg") or selectedFile.endswith(".JPG") or
          selectedFile.endswith(".png") or selectedFile.endswith(".PNG")
          ):
         pic = makePicture(selectedFile)
         show(pic)
      if selectedFile.endswith(".wav"):
         snd = makeSound(selectedFile)
         play(snd)
   #END DEF
   
   def changeDirectory(self, event):
      self.contentPane.remove(swing.JScrollPane)
      filesList = self.listFilesInDirectory()
      self.files = swing.JList(filesList)
      pane = swing.JScrollPane(self.files)
      self.contentPane.add(pane, java.awt.BorderLayout.CENTER)
      
      """
      fileView = swing.JButton("View Contents", size=(65,30),
                               actionPerformed = self.fileView)
      self.contentPane.add(fileView, java.awt.BorderLayout.EAST)
      changeDir = swing.JButton("Change Directory", size=(65,30),
                               actionPerformed = self.changeDirectory)
      self.contentPane.add(changeDir, java.awt.BorderLayout.SOUTH)
      """
      
      self.pack()
      self.visible = true
   #END DEF
   
   def listFilesInDirectory(self, directory = ""):
      if directory == "":
         chooser = swing.JFileChooser()
         chooser.setFileSelectionMode(swing.JFileChooser.DIRECTORIES_ONLY)
         chooser.setApproveButtonText("Select Folder")
         chooser.setDialogTitle("Select Folder to Show File List")
         val = None
         cancelCount = 0
         while (val != swing.JFileChooser.APPROVE_OPTION) and (cancelCount < 3):
            val = chooser.showDialog(self, None)
            if (val == swing.JFileChooser.CANCEL_OPTION):
               cancelCount += 1
         #END WHILE
         if (cancelCount == 3):
            if os.path.isdir( os.path.expanduser("~")+"/Desktop" ):
               self.currentDirectory = os.path.expanduser("~")+"/Desktop"
            else:
               self.currentDirectory = os.path.expanduser("~")+"/desktop"
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
         if ( (entry[0:1] == ".") or 
              (os.path.isdir(self.currentDirectory+"/"+entry)) or
              ((entry[-4:] != ".jpg") and (entry[-4:] != ".wav"))
            ):
            toRemove.append(entry)
         #END IF
      #END FOR
      
      for removing in toRemove:
         tempFilesList.remove(removing)
      #END FOR
      
      return tempFilesList
   #END DEF
   
   def testing(self, event):
      mywindow = swing.JFrame()
      mywindow.contentPane.add(swing.JLabel("I am here"), java.awt.BorderLayout.CENTER)
      mywindow.visible = true
   #END DEF
#END CLASS




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MAIN
fcv = FileContentsViewer()
"""
if raw_input("Continue? (y/n) ") == "y":
   fcv2 = FileContentsViewer("/Users/peterwalker/Desktop/")
"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
