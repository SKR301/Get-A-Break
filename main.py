import tkinter
import time

WorkTime = 1200								# enter the amount of time you wanna work
SnoozeTime = 300							# enter snooze time
msg = "HEY, Take a break nerd!"				# your text

def showAlert(root):
	root.title("Get-A-Break")
	root.geometry("250x100")

	var = tkinter.StringVar()
	var.set(msg)
	label = tkinter.Message( root, textvariable=var, width = 150)
	label.place(x=10, y=5)

	OK = tkinter.Button(root, text = "OK", width = 7, height = 1, command = lambda: startTimer(WorkTime, root))						#restart
	OK.place(x=100,y=50)
	Snooze = tkinter.Button(root, text = "Snooze", width = 7, height = 1, command = lambda: startTimer(SnoozeTime, root))			# snooze
	Snooze.place(x=170,y=50)

	root.mainloop()

def startTimer(timerTime, root):
	root.destroy()
	# print("Timer Started:")
	# print(timerTime)
	time.sleep(timerTime)
	
	root = tkinter.Tk()
	showAlert(root)

root = tkinter.Tk()
showAlert(root)
