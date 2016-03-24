__author__ = 'Euan Cockburn'
'speech personality project'
'File to run the openSMILe pitch configuration file'

import os

# Run the energy configuartion file
def FeatureExtract(files):
    # For each file
    for f in range(len(files)):
        # Create command
	Command = "sudo SMILExtract -C /home/euan/Documents/university/year4/speech_personality/MyConfig/gemaps/eGeMAPSv01a.conf -I " + files[f] + " -O /home/euan/Documents/university/year4/speech_personality/CSVs/eGeMAPSv01a/" + os.path.basename(files[f]) + ".csv"
	# Run command
	os.system(Command)
