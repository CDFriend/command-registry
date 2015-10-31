'''
commandregistry: Main module
Contact Charlie Friend [charles.d.friend@gmail.com] for help with this module. 

Served as a test interface for the command registry module.  Typing commands into the command line
will execute the code inside.

Copyright 2015, UVic AERO
Licensed under MIT
'''

import commandregistry

#initialize command registry
cmdReg = commandregistry.CommandRegistry()

print("\n#####UVic Aero Command Registry#####")

while(True):
	print(">> ", end="")
	cmdReg.parse(input())