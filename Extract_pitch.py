__author__ = 'Euan Cockburn'
'Speech personality project'

import glob
import os

# Function to retrieve all file names
def getfilenames():
    # Initialise list of files
    files = []

    # Retrieve all .wav files
    for f in glob.glob('/home/euan/Documents/Speech_personality/speech_personality/SSPNet-Speaker-Personality-Corpus/Audio_clips/*.wav'):
        files.append(os.path.basename(f))
    
    return files

def getpitch(files):
    # For each file
    for f in range(len(files)):
        # Create bash command
        bashCommand = "SMILExtract -C openSMILE-2.1.0/config/prosodyShs.conf -I " + files[f] + " -O CSVs/ProsodyShs/" + files[f] + ".csv"
        # Run bash command
	os.system(bashCommand)
        # Print confirmation of created file
        print "Created file, " + files[f] + ".csv"

filenames = getfilenames()
getpitch(filenames)


