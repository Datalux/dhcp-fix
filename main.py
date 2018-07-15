# !/usr/bin/python3

from tkinter import *
from tkinter import messagebox

import os

def runCommand():
	os.system("dhclient -r")
	os.system("dhclient")
	msg = messagebox.showinfo("dhcp-fix", "Fixed!")

def main():
	root = Tk()
	root.title("dhcp-fix")
	root.geometry("256x256")
	root.configure(background='#565')
	
	label = Label(root, text="Created by Datalux v0.1.1")
	label.place(relx=0.5, rely=1, anchor='s')

	if not os.geteuid() == 0:
		messagebox.showinfo("Error","This script require root privileges")
	else:
		B = Button(root, text = "Click to fix", command = runCommand)
		B.place(relx=0.5, rely=0.5, anchor=CENTER)

	root.mainloop()



if __name__ == "__main__":
	main()



