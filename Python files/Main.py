__author__ = 'Euan Cockburn'
'speech personality project'
'main file for interacting with the program'

from RunExtraction import *
from Extract_file_names import *
from ReadCSV import *

# Retrieve the names of all the .wav files
filenames = getfilenames()

# Run feature extraction configuration file on .wav files
#FeatureExtract(filenames)

# Extract contents of CSV files
ExtractCSV()

