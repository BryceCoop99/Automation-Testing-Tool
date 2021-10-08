import time
import _tkinter as Tk
from tkinter import *
from selenium import webdriver

PATH = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"


def getUsername():
    enteredUsername = username.get()
    return enteredUsername


def getPassword():
    enteredPassword = password.get()
    return enteredPassword


def openLoginPage():
    driver.get("https://gmetrix.net/")
    driver.implicitly_wait(10)


def sendLoginInfo(uid, pw):
    usernameBox = driver.find_element_by_id("body_UsernameTxtBox")
    usernameBox.clear()
    usernameBox.send_keys(uid)
    pwBox = driver.find_element_by_id("body_PasswordTxtBox")
    pwBox.clear()
    pwBox.send_keys(pw)
    driver.find_element_by_id("body_signInButton").click()


# Main entry
def startTest():
    driver = webdriver.Chrome(PATH)
    openLoginPage()
    sendLoginInfo(getUsername(), getPassword())
    time.sleep(10)
    driver.quit()

# Hide the password


def hide():
    PasswordInput.configure(show="*")
    check.configure(command=show, text="hide password")


myApp = Tk()

myApp.title = ("Automation Testing")
myApp.geometry("1000x800")

# Create background image and apply it to the window
backgroundImage = PhotoImage(file="QAProject/footer_lodyasDarktoLight.png")
backgroundLabel = Label(myApp, image=backgroundImage)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Add a menuFrame
menuFrame = LabelFrame(myApp, bg="white")
menuFrame.pack(pady=50)

# Add a title to the menuFrame
menuFrameTitle = Label(menuFrame, font=("Verdana bold", 20),
                       text="Automation Testing Tool", fg="black", bg="white")
menuFrameTitle.place(x=40, y=0)

# Add an entryFrame inside of the menuFrame
entryFrame = Frame(menuFrame, bg="gray")
entryFrame.place(x=75, y=70)

# Buttons and fields for user
usernameLabel = Label(entryFrame, font=("Verdana bold", 10),
                      text="Username:", bg="gray", fg="white")
usernameLabel.grid(row=1, column=1, padx=20)
username = Entry(entryFrame, text="Username")
username.grid(row=1, column=2, padx=20)
passwordLabel = Label(entryFrame, font=("Verdana bold", 10),
                      text="Password:", bg="gray", fg="white")
passwordLabel.grid(row=2, column=1, padx=20)
password = Entry(entryFrame, text="Password")
password.grid(row=2, column=2, padx=20)

# Create server Buttons for the menuFrame
liveButton = Button(menuFrame, text="Live", state=DISABLED, padx=56)
liveButton.grid(row=1, column=0, pady=(150, 0))
preprodButton = Button(menuFrame, text="Preprod", state=DISABLED, padx=50)
preprodButton.grid(row=1, column=1, pady=(150, 0))
stageButton = Button(menuFrame, text="Stage", state=DISABLED, padx=56)
stageButton.grid(row=1, column=2, pady=(150, 0))

# Create site Buttons for the menuFrame
studentButton = Button(menuFrame, text="Student", state=DISABLED, padx=50)
studentButton.grid(row=2, column=0, pady=(30, 0))
authorButton = Button(menuFrame, text="Author", state=DISABLED, padx=50)
authorButton.grid(row=2, column=1, pady=(30, 0))
manageButton = Button(menuFrame, text="Manage", state=DISABLED, padx=50)
manageButton.grid(row=2, column=2, pady=(30, 0))

# Create button to run the test
startButton = Button(menuFrame, text="Start", fg="black", bg="#00916E",
                     font=("Verdana bold", 10), padx=50, command=startTest)
startButton.grid(row=3, column=1, pady=(50, 10))
# Exit button to exit the program
exitButton = Button(menuFrame, text="Exit", fg="black", bg="#FA003F",
                    font=("Verdana bold", 10), padx=50)
exitButton.grid(row=3, column=2, pady=(50, 10))


myApp.mainloop()


