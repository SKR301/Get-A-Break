import tkinter
import time

WorkTime = 5		# enter the amount of time you wanna work
SnoozeTime = 3		# enter snooze time


def showAlert(root):
	root.title("Get-A-Break")
	root.geometry("500x500")

	Start = tkinter.Button(root, text ="Start", command = lambda: startTimer(WorkTime, root))
	Start.pack()
	Snooze = tkinter.Button(root, text ="Snooze", command = lambda: startTimer(SnoozeTime, root))
	Snooze.pack()
	End = tkinter.Button(root, text ="End", command = lambda: quit())
	End.pack()

	root.mainloop()

def startTimer(timerTime, root):
	root.destroy()
	print("Timer Started:")
	print(timerTime)
	time.sleep(timerTime)
	
	root = tkinter.Tk()
	showAlert(root)

root = tkinter.Tk()
showAlert(root)
