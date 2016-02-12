__author__ = 'Euan Cockburn'
'speech personality project'
'File for reading the contents of the csv file'

import csv
import glob

def ExtractCSV():
	
	filenames = []

	for files in glob.glob("/home/euan/Documents/university/year4/independant_project/speech_personality/CSVs/eGeMAPSv01a/*.csv"):
		filenames.append(files)
	
	F0semitoneamean = []; F0semitonestddevNorm = []
	F0semitonepercentile20 = []; F0semitonepercentile50 = []; F0semitonepercentile80 = []
	F0semitonepctlrange0_2 = []
	F0semitonemeanRisingSlope = []; F0semitonestddevRisingSlope = []
	F0semitonemeanFallingSlope = []; F0semitonestddevFallingSlope = []
	Loudnessamean = []; LoudnessstddevNorm = []
	Loudnesspercentile20 = []; Loudnesspercentile50 = []; Loudnesspercentile80 = []
	Loudnesspctlrange0_2 = []
	LoudnessmeanRisingSlope = []; LoudnessstddevRisingSlope = []
	LoudnessmeanFallingSlope = []; LoudnessstddevFallingSlope = []
	SpectralFluxmean = []; SpectralFluxstddev = []
	Mfcc1mean = []; Mfcc1stddevNorm = []; Mfcc2mean = []; Mfcc2stddevNorm = []
	Mfcc3mean = []; Mfcc3stddevNorm = []; Mfcc4mean = []; Mfcc4stddevNorm = []
	JitterLocalmean = []; JitterLocalstddev	= []; ShimmerLocalmean = []; ShimmerLocalstddev = []
	HNRmean = []; HNRstddev = []; LogRelF0H1H2mean = []; LogRelF0H1H2stddev = []
	LogRelF0H1A3mean = []; LogRelF0H1A3stddev = []
	F1frequencymean = []; F1frequencystddev = []; F1bandwidthmean = []; F1bandwidthstddev = []; F1amplitudeLogRelF0mean = []; F1amplitudeLogRelF0stddev = []
	F2frequencymean = []; F2frequencystddev = []; F2bandwidthmean = []; F2bandwidthstddev = []; F2amplitudeLogRelF0mean = []; F2amplitudeLogRelF0stddev = []
	F3frequencymean = []; F3frequencystddev = []; F3bandwidthmean = []; F3bandwidthstddev = []; F3amplitudeLogRelF0mean = []; F3amplitudeLogRelF0stddev = []
	AlphaRatioVmean = []; AlphaRatioVstddev = []; HammarbergIndexVmean = []; HammarbergIndexstddev = []
	SlopeV0_500mean = []; SlopeV0_500stddev = []; SlopeV500_1500mean = []; SlopeV500_1500stddev = []
	SpectralFluxVmean = []; SpectralFluxVstddev = []; Mfcc1Vmean = []; Mfcc1Vstddev = []
	Mfcc2Vmean = []; Mfcc2Vstddev = []; Mfcc3Vmean = []; Mfcc3Vstddev = []; Mfcc4Vmean = []; Mfcc4Vstddev = []
		

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
					F0semitoneamean.append(row[1]);F0semitonestddevNorm.append(row[2])
					F0semitonepercentile20.append(row[3]);F0semitonepercentile50.append(row[4]);F0semitonepercentile80.append(row[5])
					F0semitonepctlange0_2.append(row[6])
					F0semitonemeanRisingSlope.append(row[7]);F0semitonestddevRisingSlope.append(row[8])
					F0semitonemeanFallingSlope.append(row[9]);F0semitonestddevFallingSlope.append(row[10])
					Loudnessamean.append(row[11]);LoudnessstddevNorm.append(row[12])
					Loudnesspercentile20.append(row[13]);Loudnesspercentile50.append(row[14]);Loudnesspercentile80.append(row[15])
					Loudnesspctlrange0_2.append(row[16])
					LoudnessmeanRisingSlope.append(row[17]); LoudnessstddevRisingSlope.append(row[18])
					LoudnessmeanFallingSlope.append(row[19]); LoudnessstddevFallingSlope.append(row[20])
					SpectralFluxmean.append(row[21]); SpectralFluxstddev.append(row[22])
					Mfcc1mean.append(row[23]); Mfcc1stddevNorm.append(row[24])
					Mfcc2mean.append(row[25]); Mfcc2stddevNorm.append(row[26])
					Mfcc3mean.append(row[27]); Mfcc3stddevNorm.append(row[28])
					Mfcc4mean.append(row[29]); Mfcc4stddevNorm.append(row[30])
					JitterLocalmean.append(row[31]); JitterLocalstddev.append(row[32])
					ShimmerLocalmean.append(row[33]); ShimmerLocalstddev.append(row[34])
					HNRmean.append(row[35]); HNRstddev.append(row[36])
					LogRelF0H1H2mean.append(row[37]); LogRelF0H1H2stddev.append(row[38])
					F1frequencymean.append(row[39]); F1frequencystddev.append(row[40])
					F1bandwidthmean.append(row[41]); F1bandwidthstddev.append(row[42])
					F1amplitudeLogRelF0mean.append(row[43]); F1amplitudeLogRelF0stddev.append(row[44])
					F2frequencymean.append(row[45]); F2frequencystddev.append(row[46])
					F2bandwidthmean.append(row[47]); F2bandwidthstddev.append(row[48])
					F2amplitudeLogRelF0mean.append(row[49]); F2amplitudeLogRelF0stddev.append(row[50])
					F3frequencymean.append(row[51]); F3frequencystddev.append(row[52])
					F3bandwidthmean.append(row[53]); F3bandwidthstddev.append(row[54])
					F3amplitudeLogRelF0mean.append(row[55]); F3amplitudeLogRelF0stddev.append(row[56])
					AlphaRatioVmean.append(row[57]); AlphaRatioVstddev.append(row[58])
					HammarbergIndexVmean.append(row[59]); HammarbergIndexstddev.append(row[60])
					SlopeV0_500mean.append(row[61]); SlopeV0_500stddev.append(row[62])
					SlopeV500_1500mean.append(row[63]); SlopeV500_1500stddev.append(row[64])
					SpectralFluxVmean.append(row[65]); SpectralFluxVstddev.append(row[66])
					Mfcc1Vmean.append(row[67]); Mfcc1Vstddev.append(row[68])
					Mfcc2Vmean.append(row[69]); Mfcc2Vstddev.append(row[70]); Mfcc3Vmean.append(row[71])
					Mfcc3Vstddev.append(row[72]); Mfcc4Vmean.append(row[73]); Mfcc4Vstddev.append(row[74])
					

					
				
					
								
						
				
					
