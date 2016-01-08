__author__ = 'Euan Cockburn'
'speech personality project'
'File to run the openSMILe loudness configuration file'

import os

# Run the energy configuartion file
def RunLoudness(files):
    # For each file
    for f in range(len(files)):
        # Create bash command
	bashCommand = "/home/euan/Documents/university/year4/independant_project/speech_personality/SMILExtract -C /home/euan/Documents/university/year4/independant_project/speech_personality/MyConfig/Loudness.conf -I " + files[f] + " -O /home/euan/Documents/university/year4/independant_project/speech_personality/CSVs/Loudness/" + os.path.basename(files[f]) + ".csv"
	# Run bash command
	os.system(bashCommand)
