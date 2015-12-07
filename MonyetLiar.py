#! /usr/bin/monkeyrunner
'''
____________________________________________________
                                ___
      ___///___                /o o\            
     /         \               \ _ /
  /\/   0   0   \/\          ___\| \__
  \_\   _____   /_/       __/  _/^ /_  \__
     \_/ o o \_/       __/  \__________/  \__
      / _____ \       /  \________________/  \
      \_______/       \______________________/\
                                             \00o~-
____________________________________________________
@autor : hengki lodwig sirait a.k.a coltz 
android tester tools 
'''

class MonyetLiar:
	def __init__(self, dev):
		""" Initialize the clazz for testing """
		print "[+] Connecting to device"
		self.dev = dev
		self.counter = 0;

	def writeLog(self, message):
		print "[+] %s" % message

	def deleteTextMessage(self, xPosition, yPosition, action):
		""" 
		Need parameter position as operan x and y.
		The better use is locate position for x and y on right-bootom of the  edittext field 
		this assume the maximum text field is 50 char
		"""
		self.dev.touch(xPosition, yPosition, action)
		fieldLength = 50 #assume the length of text is 50 char
		self.dev.press('KEYCODE_SHIFT_LEFT', MonkeyDevice.DOWN)
		for i in range(fieldLength):
			dev.press('KEYCODE_DPAD_LEFT', MonkeyDevice.DOWN_AND_UP)
			
		MonkeyRunner.sleep(1)
		self.dev.press('KEYCODE_SHIFT_LEFT', MonkeyDevice.UP)
		self.dev.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)

	def writeText(self, xPos, yPos, action, str):
		self.dev.touch(xPos, yPos, action)
		self.dev.type(str)
		MonkeyRunner.sleep(1)

	def press(self, xPos, yPos):
		self.dev.touch(xPos, yPos, 'DOWN_AND_UP')
		MonkeyRunner.sleep(1)

	def takeImage(self, name):
		self.counter = self.counter + 1
		fname = './images/screen_capture_'
		if name :
			fname = fname + "%s_%d" % (name , self.counter)
		fname = fname + ".png"
		print fname
		img = self.dev.takeSnapshot()
		img.writeToFile(fname,'png')


#Exampleuse:
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

mon = MonyetLiar(MonkeyRunner.waitForConnection())
mon.writeLog('Starting test')
mon.press(20, 20) #will touch on the coordinate x=20 y=20
mon.takeImage("dodol")
