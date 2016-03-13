__author__ = 'Euan Cockburn'
'speech personality project'
'main file for interacting with the program'

from RunExtraction import *
from Extract_file_names import *
from ReadCSV import *
from PlotHistogram import *
from Score_Extraction import *
from Meta_Extract import *
from DictComb import *
from MetaTest import *
from ScoreTest import *

# Retrieve the names of all the .wav files
filenames = getfilenames()

# Run feature extraction configuration file on .wav files
#FeatureExtract(filenames)

# Extract contents of CSV files and assign values
features = ExtractCSV()

# Extract and process the personality scores
scores = ExtractScore()

# Extract meta data
meta = ExtractMeta()

# Merge all the dictionaries together to have a comprehensive set of information

Data = CombineDict(features, scores, meta)

# For splitting purposes a list of all feature keys
FeatureKeys = ['F0semitoneamean','F0semitonestddevNorm','F0semitonepercentile20','F0semitonepercentile50','F0semitonepercentile80','F0semitonepctlrange0_2','F0semitonemeanRisingSlope','F0semitonestddevRisingSlope','F0semitonemeanFallingSlope','F0semitonestddevFallingSlope','Loudnessamean','LoudnessstddevNorm','Loudnesspercentile20','Loudnesspercentile50','Loudnesspercentile80','Loudnesspctlrange0_2','LoudnessmeanRisingSlope','LoudnessstddevRisingSlope','LoudnessmeanFallingSlope','LoudnessstddevFallingSlope','SpectralFluxmean','SpectralFluxstddev','Mfcc1mean','Mfcc1stddevNorm','Mfcc2mean','Mfcc2stddevNorm','Mfcc3mean','Mfcc3stddevNorm','Mfcc4mean','Mfcc4stddevNorm','JitterLocalmean','JitterLocalstddev','ShimmerLocalmean','ShimmerLocalstddev','HNRmean','HNRstddev','LogRelF0H1H2mean', 
'LogRelF0H1H2stddev','LogRelF0H1A3mean','LogRelF0H1A3stddev','F1frequencymean','F1frequencystddev','F1bandwidthmean','F1bandwidthstddev','F1amplitudeLogRelF0mean','F1amplitudeLogRelF0stddev','F2frequencymean','F2frequencystddev','F2bandwidthmean','F2bandwidthstddev','F2amplitudeLogRelF0mean','F2amplitudeLogRelF0stddev','F3frequencymean','F3frequencystddev','F3bandwidthmean','F3bandwidthstddev','F3amplitudeLogRelF0mean','F3amplitudeLogRelF0stddev','AlphaRatioVmean','AlphaRatioVstddev','HammarbergIndexVmean','HammarbergIndexstddev','SlopeV0_500mean','SlopeV0_500stddev','SlopeV500_1500mean','SlopeV500_1500stddev','SpectralFluxVmean','SpectralFluxVstddev','Mfcc1Vmean','Mfcc1Vstddev','Mfcc2Vmean','Mfcc2Vstddev','Mfcc3Vmean','Mfcc3Vstddev','Mfcc4Vmean','Mfcc4Vstddev',
'AlphaRatioUVmean','HammarbergIndexUVmean','SlopeUV0-500mean','SlopeUV500-1500mean','SpectralFluxUVmean','LoudnessPeaksPerSec','VoicedSegmentsPerSec','MeanVoicedSegmentLengthSec','StddevVoicedSegmentLengthSec','MeanUnvoicedSegmentLength','StddevUnvoicedSegmentLength','EquivalentSoundLevel_dBp']

Metatest(FeatureKeys, Data)
ScoreTest(FeatureKeys, Data)

plotfeatures(features)


