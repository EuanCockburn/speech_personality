__author__ = 'Euan Cockburn'
'speech personality project'
'File to run the ProsodyShs configuration file from openSMILE'

import os

# Run the configuration file
def RunProsodyShs(files):
    # For each file
    for f in range(len(files)):
        # Create bash command
        bashCommand = "./home/euan/Documents/Speech_personality/speech_personality/SMILExtract -C MyConfig/prosodyShs.conf -I " + files[f] + " -O /home/euan/Documents/Speech_personality/speech_personality/CSVs/ProsodyShs/" + os.path.basename(files[f]) + ".csv"
        # Run bash command
	os.system(bashCommand)
