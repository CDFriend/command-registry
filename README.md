## UVic AERO Command Registry
Testbed for an extensible command-line interface for UVic Aeronautical Engineering Research Organization (AERO).

This code allows for quick creation of python commands to be accessed from a command-line environment.  It was written to allow operators control to an image processing client as it processed real-time image data being sent from an Unmanned Aerial Vehicle.

###Starting The Program
The program can be started by navigating to it's directory and typing `python main.py`.  Once the program is running, it can be stopped using Ctrl+C or by typing `exit` and pressing ENTER.

###Creating a Command
Commands can be written in [commands.py](commands.py).  Writing a command can be done as follows:
```
def testCommand(args):
	print("Hello World!")
```
The above command can then be executed by running the program and typing `testCommand`.

NOTE: Command functions must only take one parameter, or they will not be accessible through the command registry.
