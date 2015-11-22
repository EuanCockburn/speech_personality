__author__ = 'Euan Cockburn'
'Speech personality project'

import glob
import os
import csv
import matplotlib.pyplot as plt

# Function to retrieve all file names
def getfilenames():
    # Initialise list of files
    files = []

    # Retrieve all .wav files
    for f in glob.glob('/home/euan/Documents/Speech_personality/speech_personality/SSPNet-Speaker-Personality-Corpus/Audio_clips/*.wav'):
        files.append(f)
    
    return files

def RunProsodyShs(files):
    # For each file
    for f in range(len(files)):
        # Create bash command
        bashCommand = "./SMILExtract -C openSMILE-2.1.0/config/prosodyShs.conf -I " + files[f] + " -O CSVs/ProsodyShs/" + os.path.basename(files[f]) + ".csv"
        # Run bash command
	os.system(bashCommand)

def readProsodyShs():
	# Initialse list to hold names of csv files
	CSVfiles = []
	# Read all the CSV files in ProsodyShs
	for f in glob.glob('CSVs/ProsodyShs/*.csv'):
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
	return F0final_sma, VoicingFinalUnclipped_sma, pcm_loudness_sma

# Function to turn strings in lists to floats
def String2Float(Data):
	# Convert all entries to floats
	for i in range(len(Data)):
		Data[i] = float(Data[i])
		

# Function to remove the zero values from list
def removeZero(Data):
	# Return the Data without the 0 values
	return filter(lambda a: a != 0.0, Data)

# Get the average of a data set
def Averageof(Data):
	# Return the average
	return sum(Data)/len(Data)

# Plot a histogram
def plotHistogram(Data, Title, Scale):
	plt.hist(Data, bins = 50)
	plt.title(Title)
	plt.xlabel(Scale)
	plt.ylabel("Frequency")
	plt.savefig("Plots/" + Title +".png")

# Retrieve the names of all the .wav files
# filenames = getfilenames()

# Run the Prosody Shs configuration file on .wav files
# RunProsodyShs(filenames)

# Read from Prosody Shs CSV files
ProsShs_F0final, ProsShs_Voicingunclip, ProsShs_loudness = readProsodyShs()

# Remove zeros from the F0 values
ProsShs_F0final_noZero = []
for Values in ProsShs_F0final:
	ProsShs_F0final_noZero.append(removeZero(Values[:]))

# Get the average of the F0 values
ProsShs_F0final_noZero_Avg = []
for Values in ProsShs_F0final_noZero:
	ProsShs_F0final_noZero_Avg.append(Averageof(Values[:]))

plotHistogram(ProsShs_F0final_noZero_Avg, "Natural Frequency", "Hz")
