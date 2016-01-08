__author__ = 'Euan Cockburn'
'speech personality project'
'File to read the contents from the loudness CSVs'

import csv
import glob
from Utility import String2Float

def readLoudness():
	# Initialise a list to hold names of csv files
	CSVfiles = []
	# Read all CSV files in Loudness
	for f in glob.glob('/home/euan/Documents/university/year4/independant_project/speech_personality/CSVs/Loudness/*.csv'):
		CSVfiles.append(f)

	# List to hold data from CSV files
	Loudness_allfiles = []
	
	# Read the content of the CSV files
	for CSV in CSVfiles:
		with open(CSV, 'rb') as Loud:
			reader = csv.reader(Loud)
			
			firstline = True
			
			# List to hold values from CSV file
			Loudness_thisfile = []
			
			# For each row in the CSV file record the desired values
			for row in reader:
				# If on the firstline skip over it
				if firstline:
					firstline = False
					continue
			
				rows = row[0].split(';')
				Loudness_thisfile.append(rows[2])

			Loudness_allfiles.append(Loudness_thisfile)

	# Convert Strings to floats
	for entry in Loudness_allfiles:
		String2Float(entry)

	# Return the list
	return Loudness_allfiles
