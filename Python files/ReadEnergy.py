__author__ = 'Euan Cockburn'
'speech personality project'
'File to read the contents from the energy CSVs'

import csv
import glob
from Utility import String2Float

def readEnergy():
	# Initialise a list to hold names of csv files
	CSVfiles = []
	# Read all CSV files in Energy
	for f in glob.glob('/home/euan/Documents/university/year4/independant_project/speech_personality/CSVs/Energy/*.csv'):
		CSVfiles.append(f)

	# List to hold data from CSV files
	Energy_allfiles = []
	
	# Read the content of the CSV files
	for CSV in CSVfiles:
		with open(CSV, 'rb') as Eng:
			reader = csv.reader(Eng)
			
			firstline = True
			
			# List to hold values from CSV file
			Energy_thisfile = []
			
			# For each row in the CSV file record the desired values
			for row in reader:
				# If on the firstline skip over it
				if firstline:
					firstline = False
					continue
			
				rows = row[0].split(';')
				Energy_thisfile.append(rows[2])

			Energy_allfiles.append(Energy_thisfile)

	# Convert Strings to floats
	for entry in Energy_allfiles:
		String2Float(entry)

	# Return the list
	return Energy_allfiles
