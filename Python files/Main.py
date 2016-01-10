__author__ = 'Euan Cockburn'
'speech personality project'
'main file for interacting with the program'

from Extract_file_names import *
from Extract_loudness import *
from ReadLoudness import *
from RunLoudness import *
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

# Run pitch extraction configuration file on .wav files
RunPitch(filenames)

# Run loudness extraction
RunLoudness(filenames)

# Run the energy file
RunEnergyConfig(filenames)

# Read the data from Loudness CSV files
Loudness = readLoudness()
# Read the data from energy CSV files
Energy = readEnergy()
# Read the data from the pitch files
Pitch, jitter = readPitch()

# Extract the averaged pitch and pitch jitter from the Pitch data files
Pitch_avg, jitter_avg = RetrievePitch(Pitch, jitter)

# Extract the averaged loudness from the Prosody data files
Loudness_avg = RetrieveLoudness(Loudness)

# Extract the averaged energy from the Energy data
Energy_avg = RetrieveEnergy(Energy)

# Plot the histogram of the pitch
plotHistogram(Pitch_avg, "Natural Frequency", "Hz")
plotHistogram(Loudness_avg, "loudness", " ")
plotHistogram(Energy_avg, "Energy", " ")
plotHistogram(jitter_avg, "Jitter", " ")



