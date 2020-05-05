import _thread
import os
import subprocess, win32con, win32api
from pynput.mouse import Button, Controller

manter = True

def task(task_name, delay):
	global manter
	print("Thread : %s" % (task_name))

	if(task_name == "1"):
		valor = input("Digite T para sair... ")
		if (valor == "T"):

			manter = False
	if(task_name == "2"):

		while (manter):
			mouse = Controller()
			print('The current pointer position is {0}'.format(
			    mouse.position))

			win32api.SetCursorPos((800, 300))

os.system("pause")

_thread.start_new_thread(task, ("1",0))




