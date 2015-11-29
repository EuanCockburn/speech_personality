__author__ = 'Euan Cockburn'
'Speech personality project'
'File to extract the pitch from the Prosody configured files'

from Utility import *

def RetrievePitch(ProsShs_F0final):
    # Remove zeros from the F0 values
    ProsShs_F0final_noZero = []
    for Values in ProsShs_F0final:
	    ProsShs_F0final_noZero.append(removeZero(Values[:]))

    # Get the average of the F0 values
    ProsShs_F0final_noZero_Avg = []
    for Values in ProsShs_F0final_noZero:
	    ProsShs_F0final_noZero_Avg.append(Averageof(Values[:]))

    return ProsShs_F0final_noZero_Avg


