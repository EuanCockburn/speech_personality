__author__ = 'Euan Cockburn'
'Speech personality project'
'Average the energy of the voice file signals'

from Utility import *

def RetrieveEnergy(EnergyData):
    # Get the average of the loudness values
    energyAvg = []
    for Values in EnergyData:
	    energyAvg.append(Averageof(Values[:]))
	    for entry in Values:
		if entry < 0:
			print entry
    return energyAvg
