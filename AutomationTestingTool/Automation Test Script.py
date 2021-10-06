from tkinter import *

myApp = Tk()

myApp.title = "Automation Testing"
myApp.geometry("1000x800")

#Create background image and apply it to the window
backgroundImage = PhotoImage(file="footer_lodyasDarktoLight.png")
backgroundLabel = Label(myApp, image=backgroundImage)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

#Add a titleFrame to the menuFrame
menuFrame = Frame(myApp, bg="white")
menuFrame.pack()

#Add a title to the Frame
menuFrameTitle = Label(myApp, font=("Verdana bold", 20), text="Automation Testing Tool", fg="black", bg="white")
menuFrameTitle.grid(row=0, column=0, padx=10)

#Add an entryFrame inside of the menuFrame
entryFrame = Frame(menuFrame, bg="gray")
entryFrame.place(x=100, y=50)

#Add a Button Frame to the menuFrame


#Buttons and fields for user
usernameLabel = Label(entryFrame, font=("Verdana bold", 10), text="Username:", bg="gray", fg="white")
usernameLabel.grid(row=1, column=1, padx=20)
usernameInput = Entry(entryFrame, text="Username")
usernameInput.grid(row=1, column=2, padx=20)
passwordLabel = Label(entryFrame, font=("Verdana bold", 10), text="Password:", bg="gray", fg="white")
passwordLabel.grid(row=2, column=1, padx=20)
passwordInput = Entry(entryFrame, text="Password")
passwordInput.grid(row=2, column=2, padx=20)

#Buttons and fields for password

#Create Buttons for the menuFrame
liveButton = Button(menuFrame, text="Live", state=DISABLED, padx=50)
liveButton.grid(row=3, column=0, pady=75)
preprodButton = Button(menuFrame, text="Preprod", state=DISABLED, padx=50)
preprodButton.grid(row=3, column=1, pady=75)
stageButton = Button(menuFrame, text="Stage", state=DISABLED, padx=50)
stageButton.grid(row=3, column=2, pady=75)

#Exit button to exit the program
exitButton = Button(myApp, text="Exit", fg="red")
exitButton.pack(pady=100)


myApp.mainloop()

