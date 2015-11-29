__author__ = 'Euan Cockburn'
'speech personality project'
'Utility file to hold helper functions'

# Function to turn a list of strings into a list of floats
def String2Float(Data):
	# Convert all entries to floats
	for i in range(len(Data)):
		Data[i] = float(Data[i])

# Function to remove the zero values from a list
def removeZero(Data):
	# Return the Data without the 0 values
	return filter(lambda a: a != 0.0, Data)

# Get the average of a list
def Averageof(Data):
	# Return the average
	return sum(Data)/len(Data)
