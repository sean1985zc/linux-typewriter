#!/usr/bin/env python 
## Play sounds on keypresses in Linux
## Originally by Sayan "Riju" Chakrabarti (sayanriju) 
## http://rants.sayanriju.co.cc/script-to-make-tick-tick-sound-on-keypres
 
from Xlib.display import Display 
import threading
import os 
import time

notes=[440,494,523,587,659,698,784]
 
ZERO,SHIFT,ALT,CTL,BACK,SPACE,ENTER,SC=[],[],[],[],[],[],[],[] 
for i in range(0,32): 
	ZERO.append(0) 
	if i==4: 
		ENTER.append(16) 
	else: 
		ENTER.append(0)
	if i==8: 
		SPACE.append(2) 
	else: 
		SPACE.append(0)
	if i==2: 
		BACK.append(64) 
	else: 
		BACK.append(0)
	if i==6: 
		SHIFT.append(4) 
	else: 
		SHIFT.append(0) 
	if i==4: 
		CTL.append(32) 
	else: 
		CTL.append(0) 
	if i==8: 
		ALT.append(1) 
	else: 
		ALT.append(0) 
	if i==6: 
		SC.append(4)
	elif i==4:
		SC.append(32)
	else: 
		SC.append(0) 
		 
ignorelist=[ZERO,ALT,SHIFT,CTL,SC] #
# ignorelist=[ZERO]

class KeyPress(threading.Thread):
	def run(self):
		os.system("aplay /local/cz12g09/Software/keypress/sounds/keyn.wav")

class BackKeyPress(threading.Thread):
	def run(self):
		os.system("aplay /local/cz12g09/Software/keypress/sounds/Back.wav")

class SpaceKeyPress(threading.Thread):
	def run(self):
		os.system("aplay /local/cz12g09/Software/keypress/sounds/Space.wav")
		
class EnterKeyPress(threading.Thread):
	def run(self):
		os.system("aplay /local/cz12g09/Software/keypress/sounds/typewriterding.wav")
		
def main(): 
	disp = Display()
	while 1:
		keymap = disp.query_keymap() 
		if keymap not in ignorelist: 
			if keymap==BACK:
				BackKeyPress().start()
			elif keymap==SPACE:
				SpaceKeyPress().start()
			elif keymap==ENTER:
				EnterKeyPress().start()
			else:
				KeyPress().start()
			time.sleep(0.2)
		else:
			time.sleep(0.02)
 
if __name__ == '__main__': 
	main() 
