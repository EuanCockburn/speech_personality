__author__ = 'Euan Cockburn'
'speech personality project'
'main file for interacting with the program'

from Extract_file_names import *
from RunProsodyShs import *
from ReadProsodyFiles import *
from PlotHistogram import *
from Extract_pitch import *
from RunPitch import *
from ReadPitch import *
from Extract_loudness import *
from RunEnergy import *
from ReadEnergy import *
from Extract_energy import *

# Retrieve the names of all the .wav files
filenames = getfilenames()

# Run the Prosody Shs configuration file on .wav files
#RunProsodyShs(filenames)

# Run pitch extraction configuration file on .wav files
RunPitch(filenames)

# Run the energy file
#RunEnergyConfig(filenames)

# Read the data from Prosody Shs CSV files
ProsShs_Voicingunclip, ProsShs_loudness = readProsodyShs()
# Read the data from energy CSV files
Energy = readEnergy()
# Read the data from the pitch files
Pitch, jitter = readPitch()
# Extract the averaged pitch and pitch jitter from the Pitch data files
Pitch_avg, jitter_avg = RetrievePitch(Pitch, jitter)

# Extract the averaged loudness from the Prosody data files
ProsShs_loudness_avg = RetrieveLoudness(ProsShs_loudness)

# Extract the averaged energy from the Energy data
Energy_avg = RetrieveEnergy(Energy)

# Plot the histogram of the pitch
plotHistogram(Pitch_avg, "Natural Frequency", "Hz")
plotHistogram(ProsShs_loudness_avg, "loudness", " ")
plotHistogram(Energy_avg, "Energy", " ")
plotHistogram(jitter_avg, "Jitter", " ")



