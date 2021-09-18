import tkinter
import time

WorkTime = 20																	# enter the amount of time you wanna work
SnoozeTime = 10																	# enter snooze time
CustomTime = 0
msg = "HEY, Take a break NERD!"													# your text

def showAlert(root):
	root.title("Get-A-Break")
	root.geometry("250x100+750+500")

	alertMsg = tkinter.StringVar()												#Alert MSG
	alertMsg.set(msg)
	label = tkinter.Message( root, textvariable=alertMsg, width = 150)
	label.place(x=10, y=5)

	enterLabel = tkinter.StringVar()											#new timer label
	enterLabel.set("Enter New Time (mints):")
	newTimelabel = tkinter.Message( root, textvariable=enterLabel, width = 150)
	newTimelabel.pack_forget()

	newTimeInput = tkinter.Entry(root, width = 25)								#new timer input box
	newTimeInput.pack_forget()

	newTimeOK = tkinter.Button(root, text = "OK", width = 7, height = 1, command = lambda: startTimer(newTimeInput.get(), root))
	newTimeOK.pack_forget()

	dropup_img = tkinter.PhotoImage(file = "./drawable/dropup_btn.png")			#button to show custom timer (v)
	dropup_btn = tkinter.Button(root, image = dropup_img, borderwidth = 0, command = lambda: hideNewTimeOption(newTimelabel, newTimeInput, newTimeOK, dropdown_btn, dropup_btn, root))
	dropup_btn.place(x=25,y=55)

	dropdown_img = tkinter.PhotoImage(file = "./drawable/dropdown_btn.png")		#button to hide custom timer (^)
	dropdown_btn = tkinter.Button(root, image = dropdown_img, borderwidth = 0, command = lambda: showNewTimeOption(newTimelabel, newTimeInput, newTimeOK, dropdown_btn, dropup_btn, root))
	dropdown_btn.place(x=25,y=55)

	OK = tkinter.Button(root, text = "OK", width = 7, height = 1, command = lambda: startTimer(WorkTime, root))						#restart
	OK.place(x=100,y=50)
	Snooze = tkinter.Button(root, text = "Snooze", width = 7, height = 1, command = lambda: startTimer(SnoozeTime, root))			# snooze
	Snooze.place(x=170,y=50)

	root.mainloop()

#starts the clock
def startTimer(timerTime, root):
	root.destroy()
	try:
		timerTime = int(timerTime) * 60
	except:
		timerTime = SnoozeTime * 60

	time.sleep(timerTime)
	
	root = tkinter.Tk()
	showAlert(root)

#show custom timer
def showNewTimeOption(newTimelabel, newTimeInput, newTimeOK, dropdown_btn, dropup_btn, root):
	root.geometry("250x150+750+500")
	newTimelabel.place(x=10, y=85)
	newTimeInput.place(x=15, y=110)
	newTimeOK.place(x=175,y=105)

	dropdown_btn.place_forget()	
	dropup_btn.place(x=25,y=55)

#hide custom timer
def hideNewTimeOption(newTimelabel, newTimeInput, newTimeOK, dropdown_btn, dropup_btn, root):
	root.geometry("250x100+750+500")
	newTimelabel.place_forget()
	newTimeInput.place_forget()
	newTimeOK.place_forget()

	dropup_btn.place_forget()
	dropdown_btn.place(x=25,y=55)


root = tkinter.Tk()
showAlert(root)
