__author__ = 'Euan Cockburn'
'Speech personality project'
'File to extract the pitch from the Prosody configured files'

from Utility import *

def RetrievePitch(Pitch, Jitter, Shimmer, Formant1, Formant2, Formant3):
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

    Shimmer_noZero = []
    for Values in Shimmer_noZero:
	Shimmer_noZero.append(removeZero(Values[:]))

    Shimmer_Avg = []
    for Values in Shimmer_noZero:
	Shimmer_Avg.append(Averageof(Values[:]))

    Formant1_Avg = []
    Formant2_Avg = []
    Formant3_Avg = []
    for Values in Formant1:
	Formant1_Avg.append(Averageof(Values[:]))

    for Values in Formant2:
	Formant2_Avg.append(Averageof(Values[:]))
    
    for Values in Formant3:
	Formant3_Avg.append(Averageof(Values[:]))

    return Pitch_Avg, Jitter_Avg, Shimmer_Avg, Formant1_Avg, Formant2_Avg, Formant3_Avg


