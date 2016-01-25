__author__ = 'Euan Cockburn'
'speech personality project'
'File to read the contents from the pitch CSVs'

import csv
import glob
from Utility import String2Float

def readPitch():
	# Initialise a list to hold names of csv files
	CSVfiles = []
	# Read all CSV files in Pitch
	for f in glob.glob('/home/euan/Documents/university/year4/independant_project/speech_personality/CSVs/Pitch/*.csv'):
		CSVfiles.append(f)

	# List to hold data from CSV files
	Pitch_allfiles = []
	Jitter_allfiles = []
	Shimmer_allfiles = []
	Formant1_allfiles = []
	Formant2_allfiles = []
	Formant3_allfiles = []
	# Read the content of the CSV files
	for CSV in CSVfiles:
		with open(CSV, 'rb') as Pit:
			reader = csv.reader(Pit)
			
			firstline = True
			
			# List to hold values from CSV file
			Pitch_thisfile = []
			Jitter_thisfile = []
			Shimmer_thisfile = []
			Formant1_thisfile = []
			Formant2_thisfile = []
			Formant3_thisfile = []
			# For each row in the CSV file record the desired values
			for row in reader:
				# If on the firstline skip over it
				if firstline:
					firstline = False
					continue
			
				rows = row[0].split(';')
				Pitch_thisfile.append(rows[2])
				Jitter_thisfile.append(rows[4])
				Shimmer_thisfile.append(rows[5])
				Formant1_thisfile.append(rows[6])
				Formant2_thisfile.append(rows[7])
				Formant3_thisfile.append(rows[8])

			Pitch_allfiles.append(Pitch_thisfile)
			Jitter_allfiles.append(Jitter_thisfile)
			Shimmer_allfiles.append(Shimmer_thisfile)
			Formant1_allfiles.append(Formant1_thisfile)
			Formant2_allfiles.append(Formant2_thisfile)
			Formant3_allfiles.append(Formant3_thisfile)

	# Convert Strings to floats
	for entry in Pitch_allfiles:
		String2Float(entry)

	for entry in Jitter_allfiles:
		String2Float(entry)

	for entry in Formant1_allfiles:
		String2Float(entry)

	for entry in Formant2_allfiles:
		String2Float(entry)

	for entry in Formant3_allfiles:
		String2Float(entry)

	for entry in Shimmer_allfiles:
		String2Float(entry)

	# Return the list
	return Pitch_allfiles, Jitter_allfiles, Shimmer_allfiles, Formant1_allfiles, Formant2_allfiles, Formant3_allfiles
