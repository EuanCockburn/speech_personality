__author__ = 'Euan Cockburn'
'speech personality project'
'main file for interacting with the program'

from Extract_file_names import *
from RunProsodyShs import *
from ReadProsodyFiles import *
from PlotHistogram import *
from Extract_pitch import *
from Extract_loudness import *

# Retrieve the names of all the .wav files
filenames = getfilenames()

# Run the Prosody Shs configuration file on .wav files
RunProsodyShs(filenames)

# Run the energy file
RunEnergyConfig(filenames)

# Read the data from Prosody Shs CSV files
ProsShs_F0final, ProsShs_Voicingunclip, ProsShs_loudness = readProsodyShs()

# Extract the averaged pitch from the Prosody data files
ProsShs_F0final_noZero_Avg = RetrievePitch(ProsShs_F0final)

# Extract the averaged loudness from the Prosody data files
ProsShs_loudness_avg = RetrieveLoudness(ProsShs_loudness)

# Plot the histogram of the pitch
plotHistogram(ProsShs_F0final_noZero_Avg, "Natural Frequency", "Hz")
plotHistogram(ProsShs_loudness_avg, "loudness", " ")



