__author__ = 'Euan Cockburn'
'speech personality project'
'main file for interacting with the program'

from Extract_file_names import *
from RunProsodyShs import *
from ReadProsodyFiles import *
from PlotHistogram import *
from Extract_pitch import *
from Extract_loudness import *
from RunEnergy import *
from ReadEnergy import *
from Extract_energy import *

# Retrieve the names of all the .wav files
filenames = getfilenames()

# Run the Prosody Shs configuration file on .wav files
RunProsodyShs(filenames)

# Run the energy file
RunEnergyConfig(filenames)

# Read the data from Prosody Shs CSV files
ProsShs_F0final, ProsShs_Voicingunclip, ProsShs_loudness = readProsodyShs()
# Read the data from energy CSV files
Energy = readEnergy()

# Extract the averaged pitch from the Prosody data files
ProsShs_F0final_noZero_Avg = RetrievePitch(ProsShs_F0final)

# Extract the averaged loudness from the Prosody data files
ProsShs_loudness_avg = RetrieveLoudness(ProsShs_loudness)

# Extract the averaged energy from the Energy data
Energy_avg = RetrieveEnergy(Energy)

# Plot the histogram of the pitch
plotHistogram(ProsShs_F0final_noZero_Avg, "Natural Frequency", "Hz")
plotHistogram(ProsShs_loudness_avg, "loudness", " ")
plotHistogram(Energy_avg, "Energy", " ")



