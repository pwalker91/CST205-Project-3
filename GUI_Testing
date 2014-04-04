
# # # # # # # # # # # # # # #
# This is the function that starts the GUI
#  for the user to use
def run_GUI():
   #printNow("I am in the GUI!!\n")
   
   win = swing.JFrame("File Contents Viewer",size=(200,200))
   win.visible = true
   
   field = swing.JTextField( preferredSize=(200,20), 
                             minimumSize=(75,20) )
   field.text = "I am trying out Swing!!"
   win.contentPane.add(field)
   win.visible = true
   button = swing.JButton("View Contents",
                          preferredSize=(200,20),
                          minimumSize=(75,20) )
   win.contentPane.add(button)
   win.visible = true
   win.pack()
   win.visible = true

# END DEF



# # # # # # # # # # # # # # #
# MAIN
ans = raw_input("Would you like to run the GUI? (y/n) ")
if ans == "y":
   run_GUI()
# END MAIN