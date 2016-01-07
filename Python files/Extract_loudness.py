__author__ = 'Euan Cockburn'
'Speech personality project'
'Average the loudness of the voice file signals'

from Utility import *

def RetrieveLoudness(LoudnessData):
    # Get the average of the loudness values
    loudnessAvg = []
    for Values in LoudnessData:
	    loudnessAvg.append(Averageof(Values[:]))

    return loudnessAvg
