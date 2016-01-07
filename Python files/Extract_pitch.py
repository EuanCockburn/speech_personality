__author__ = 'Euan Cockburn'
'Speech personality project'
'File to extract the pitch from the Prosody configured files'

from Utility import *

def RetrievePitch(Pitch, Jitter):
    # Remove zeros from the F0 and jitter values
    Pitch_noZero = []
    for Values in Pitch:
	Pitch_noZero.append(removeZero(Values[:]))
    
    Jitter_noZero = []
    for Values in Jitter:
	Jitter_noZero.append(removeZero(Values[:]))

    # Get the average of the F0 and jitter values
    Pitch_Avg = []
    for Values in Pitch_noZero:
	Pitch_Avg.append(Averageof(Values[:]))

    Jitter_Avg = []
    for Values in Jitter_noZero:
	Jitter_Avg.append(Averageof(Values[:]))

    return Pitch_Avg


