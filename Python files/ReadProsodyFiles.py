__author__ = 'Euan Cockburn'
'speech personality project'
'File to read the contents from the ProsodyShs configured CSVs'

import csv
import glob
from Utility import String2Float

def readProsodyShs():
	# Initialse list to hold names of csv files
	CSVfiles = []
	# Read all the CSV files in ProsodyShs
	for f in glob.glob('/home/euan/Documents/university/year4/independant_project/speech_personality/CSVs/ProsodyShs/*.csv'):
		CSVfiles.append(f)
	
	# Lists to data from CSV files
	F0final_sma = []
	VoicingFinalUnclipped_sma = []
	pcm_loudness_sma = []

	# Read the contents of all the CSV files
	for CSVfile in CSVfiles:
	    	with open(CSVfile, 'rb') as Prosod:
			reader = csv.reader(Prosod)
			
			firstline = True
			
			# Lists to hold values from CSV files
			F0 = []
			Voicing = []
			loudness = []
			
			# For each row in the CSV file record the desired values
			for row in reader:
				# If on the firstline skip over it
				if firstline:
					firstline = False
					continue

				rows = row[0].split(';')
				F0.append(rows[2])
				Voicing.append(rows[3])
				loudness.append(rows[4])
			
			F0final_sma.append(F0)
			VoicingFinalUnclipped_sma.append(Voicing)
			pcm_loudness_sma.append(loudness)
	
	# Convert Strings to floats and remove title strings
	for entry in F0final_sma:
		String2Float(entry)
	for entry in VoicingFinalUnclipped_sma:
		String2Float(entry)
	for entry in pcm_loudness_sma:
		String2Float(entry)

	# Return the lists
	return VoicingFinalUnclipped_sma, pcm_loudness_sma
