'''
commandregistry: Command Registry module
Processes incoming command strings from the System Analyst client.  All commands and their 
source code can be created and edited in commands.py.  
Contact Charlie Friend [charles.d.friend@gmail.com] for help with this module. 

Copyright 2015, UVic AERO
Licensed under MIT
'''

import sys, inspect
import commands

class CommandRegistry(object):
	#Initializes the command registry object and finds all usable commands.
	def __init__(self):
		self.cmdReg = {} #dictionary for name/command pairs
		
		#get functions in commands.py
		members = inspect.getmembers(sys.modules["commands"], inspect.isfunction) 
		for name, obj in members:
			if len(inspect.getargspec(obj).args) == 1:
				self.cmdReg.update({name : obj}) #add if 1 parameter is required
			else:
				print("Command " + name + " failed to initialize")

	#Finds the command requested by an incoming JSON packet in the registry and executes the code.
	def parse(self, commandString):
		#split the command string into the command name and arguments
		splitInput = commandString.split(" ")
		if splitInput[0] in self.cmdReg:
			#TODO: add error handling and logging capabilities here
			cmdName = splitInput[0]
			if (len(splitInput) > 1):
				splitInput.remove(cmdName) #list of arguments
			self.cmdReg[cmdName](splitInput) #execute the code
		else:
			#TODO: integrate error messages into the logging system
			print("Command not found.")