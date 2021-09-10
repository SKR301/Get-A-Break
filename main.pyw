# TODO: addd NEWtimerOK

import tkinter
import time

WorkTime = 5								# enter the amount of time you wanna work
SnoozeTime = 1								# enter snooze time
CustomTime = 0
msg = "HEY, Take a break nerd!"				# your text

def showAlert(root):
	root.title("Get-A-Break")
	root.geometry("250x100")

	alertMsg = tkinter.StringVar()
	alertMsg.set(msg)
	label = tkinter.Message( root, textvariable=alertMsg, width = 150)
	label.place(x=10, y=5)

	enterLabel = tkinter.StringVar()
	enterLabel.set("Enter New Time (mints):")
	newTimelabel = tkinter.Message( root, textvariable=enterLabel, width = 150)
	newTimelabel.pack_forget()

	newTimeInput = tkinter.Entry(root, width = 25)
	newTimeInput.pack_forget()

	# var.set("C")
	# newTimeOK = tkinter.Message( root, textvariable=var, width = 150)
	# # newTimeOK.place(x=50, y=100)
	# newTimeOK.pack_forget()

	dropup_img = tkinter.PhotoImage(file = "./drawable/dropup_btn.png")
	dropup_btn = tkinter.Button(root, image = dropup_img, borderwidth = 0, command = lambda: hideNewTimeOption(newTimelabel, newTimeInput, dropdown_btn, dropup_btn))
	dropup_btn.place(x=25,y=55)

	dropdown_img = tkinter.PhotoImage(file = "./drawable/dropdown_btn.png")
	dropdown_btn = tkinter.Button(root, image = dropdown_img, borderwidth = 0, command = lambda: showNewTimeOption(newTimelabel, newTimeInput, dropdown_btn, dropup_btn))
	dropdown_btn.place(x=25,y=55)

	OK = tkinter.Button(root, text = "OK", width = 7, height = 1, command = lambda: startTimer(WorkTime, root))						#restart
	OK.place(x=100,y=50)
	Snooze = tkinter.Button(root, text = "Snooze", width = 7, height = 1, command = lambda: startTimer(SnoozeTime, root))			# snooze
	Snooze.place(x=170,y=50)

	root.mainloop()

def startTimer(timerTime, root):
	root.destroy()
	print("Timer Started:")
	print(timerTime)
	# time.sleep(timerTime)
	
	root = tkinter.Tk()
	showAlert(root)

def showNewTimeOption(newTimelabel, newTimeInput, dropdown_btn, dropup_btn):
	newTimelabel.place(x=10, y=75)
	newTimeInput.place(x=15, y=95)

	dropdown_btn.place_forget()	
	dropup_btn.place(x=25,y=55)


def hideNewTimeOption(newTimelabel, newTimeInput, dropdown_btn, dropup_btn):
	newTimelabel.place_forget()
	newTimeInput.place_forget()

	dropup_btn.place_forget()
	dropdown_btn.place(x=25,y=55)


root = tkinter.Tk()
showAlert(root)
