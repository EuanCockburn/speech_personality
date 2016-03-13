__author__ = 'Euan Cockburn'
'speech personality project'
'File for reading the contents of the csv file'

import csv
import glob

def ExtractCSV():
	filenames = []
				
	for files in glob.glob("/home/euan/Documents/university/year4/speech_personality/CSVs/eGeMAPSv01a/*.csv"):
		filenames.append(files)
	features = []
	
	for name in filenames:
		with open(name, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				# If the row is empty move on to next row
				if row == []:
					continue
				# If the row does not start with 'unknown' move to next row
				elif row[0] != "'unknown'":
					continue
				# If the row does start with an 'unknown' begin reading the content of the row
				else:
					results = {	'Name': name[74:-8], 
						   	'F0semitoneamean': (float(row[1])), 
						   	'F0semitonestddevNorm': (float(row[2])), 
						   	'F0semitonepercentile20':(float(row[3])),
							'F0semitonepercentile50':(float(row[4])),
							'F0semitonepercentile80':(float(row[5])), 
							'F0semitonepctlrange0_2':(float(row[6])), 
							'F0semitonemeanRisingSlope':(float(row[7])), 
							'F0semitonestddevRisingSlope':(float(row[8])), 
							'F0semitonemeanFallingSlope':(float(row[9])), 
							'F0semitonestddevFallingSlope':(float(row[10])), 
							'Loudnessamean':(float(row[11])),
							'LoudnessstddevNorm':(float(row[12])),
							'Loudnesspercentile20':(float(row[13])), 
							'Loudnesspercentile50':(float(row[14])), 
							'Loudnesspercentile80':(float(row[15])),
							'Loudnesspctlrange0_2':(float(row[16])), 
							'LoudnessmeanRisingSlope':(float(row[17])), 
							'LoudnessstddevRisingSlope':(float(row[18])),
							'LoudnessmeanFallingSlope':(float(row[19])), 
							'LoudnessstddevFallingSlope':(float(row[20])), 
							'SpectralFluxmean':(float(row[21])), 
							'SpectralFluxstddev':(float(row[22])), 
							'Mfcc1mean':(float(row[23])), 
							'Mfcc1stddevNorm':(float(row[24])), 
							'Mfcc2mean':(float(row[25])), 
							'Mfcc2stddevNorm':(float(row[26])), 
							'Mfcc3mean':(float(row[27])), 
							'Mfcc3stddevNorm':(float(row[28])), 
							'Mfcc4mean':(float(row[29])), 
							'Mfcc4stddevNorm':(float(row[30])), 
							'JitterLocalmean':(float(row[31])), 
							'JitterLocalstddev':(float(row[32])), 
							'ShimmerLocalmean':(float(row[33])), 
							'ShimmerLocalstddev':(float(row[34])), 
							'HNRmean':(float(row[35])), 
							'HNRstddev':(float(row[36])), 
							'LogRelF0H1H2mean': (float(row[37])), 
							'LogRelF0H1H2stddev': (float(row[38])),
							'LogRelF0H1A3mean': (float(row[39])),
							'LogRelF0H1A3stddev': (float(row[40])),
							'F1frequencymean': (float(row[41])), 
							'F1frequencystddev': (float(row[42])), 
							'F1bandwidthmean': (float(row[43])), 
							'F1bandwidthstddev': (float(row[44])), 
							'F1amplitudeLogRelF0mean': (float(row[45])), 
							'F1amplitudeLogRelF0stddev': (float(row[46])), 
							'F2frequencymean': (float(row[47])), 
							'F2frequencystddev': (float(row[48])), 
							'F2bandwidthmean': (float(row[49])), 
							'F2bandwidthstddev': (float(row[50])), 
							'F2amplitudeLogRelF0mean': (float(row[51])), 
							'F2amplitudeLogRelF0stddev': (float(row[52])), 
							'F3frequencymean': (float(row[53])), 
							'F3frequencystddev': (float(row[54])), 
							'F3bandwidthmean': (float(row[55])), 
							'F3bandwidthstddev': (float(row[56])), 
							'F3amplitudeLogRelF0mean': (float(row[57])), 
							'F3amplitudeLogRelF0stddev': (float(row[58])), 
							'AlphaRatioVmean': (float(row[59])), 
							'AlphaRatioVstddev': (float(row[60])), 
							'HammarbergIndexVmean': (float(row[61])), 
							'HammarbergIndexstddev': (float(row[62])), 
							'SlopeV0_500mean': (float(row[63])), 
							'SlopeV0_500stddev': (float(row[64])), 
							'SlopeV500_1500mean': (float(row[65])), 
							'SlopeV500_1500stddev': (float(row[66])), 
							'SpectralFluxVmean': (float(row[67])), 
							'SpectralFluxVstddev': (float(row[68])), 
							'Mfcc1Vmean': (float(row[69])), 
							'Mfcc1Vstddev': (float(row[70])), 
							'Mfcc2Vmean': (float(row[71])), 
							'Mfcc2Vstddev': (float(row[72])), 
							'Mfcc3Vmean': (float(row[73])), 
							'Mfcc3Vstddev': (float(row[74])), 
							'Mfcc4Vmean': (float(row[75])), 
							'Mfcc4Vstddev': (float(row[76])),
							'AlphaRatioUVmean': (float(row[77])),
							'HammarbergIndexUVmean': (float(row[78])),
							'SlopeUV0-500mean': (float(row[79])),
							'SlopeUV500-1500mean': (float(row[80])),
							'SpectralFluxUVmean': (float(row[81])),
							'LoudnessPeaksPerSec': (float(row[82])),
							'VoicedSegmentsPerSec': (float(row[83])),
							'MeanVoicedSegmentLengthSec': (float(row[84])),
							'StddevVoicedSegmentLengthSec': (float(row[85])),
							'MeanUnvoicedSegmentLength': (float(row[86])),
							'StddevUnvoicedSegmentLength': (float(row[87])),
							'EquivalentSoundLevel_dBp': (float(row[88]))}

			features.append(results) 

	return features
