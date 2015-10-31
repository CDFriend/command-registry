'''
commandregistry: Commands module
Contains all of the commands to be accessed by the CommandRegistry module.  
Contact Charlie Friend [charles.d.friend@gmail.com] for help with this module. 

The command registry will attempt to initialize every function written in this 
file.  Each function must contain only one parameter "args", which will contain
a list of the arguments following the command name. 

NOTE: If more than one parameter is used in a function, it will not be accessible
      from the command registry!

Copyright 2015, UVic AERO
Licensed under MIT
'''

#IMPORTS
import sys

#COMMANDS

'''
EXAMPLE COMMAND: for testing and demonstration purposes
e.g. "printArgs x y z" will access the printArgs function.  
     args: [x, y, z]
'''
def printArgs(args):
	print(args)
	
def exit(args):
	sys.exit() #exit the application