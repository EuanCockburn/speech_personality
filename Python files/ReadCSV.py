__author__ = 'Euan Cockburn'
'speech personality project'
'File for reading the contents of the csv file'

import csv
import glob

def ExtractCSV():
	filenames = []
	
	for files in glob.glob("/home/euan/Documents/university/year4/speech_personality/CSVs/eGeMAPSv01a/*.csv"):
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
					F0semitoneamean.append(int(float(row[1])));F0semitonestddevNorm.append(int(float(row[2])))
					F0semitonepercentile20.append(int(float(row[3])));F0semitonepercentile50.append(int(float(row[4])));F0semitonepercentile80.append(int(float(row[5])))
					F0semitonepctlrange0_2.append(int(float(row[6])))
					F0semitonemeanRisingSlope.append(int(float(row[7])));F0semitonestddevRisingSlope.append(int(float(row[8])))
					F0semitonemeanFallingSlope.append(int(float(row[9])));F0semitonestddevFallingSlope.append(int(float(row[10])))
					Loudnessamean.append(int(float(row[11])));LoudnessstddevNorm.append(int(float(row[12])))
					Loudnesspercentile20.append(int(float(row[13])));Loudnesspercentile50.append(int(float(row[14])));Loudnesspercentile80.append(int(float(row[15])))
					Loudnesspctlrange0_2.append(int(float(row[16])))
					LoudnessmeanRisingSlope.append(int(float(row[17]))); LoudnessstddevRisingSlope.append(int(float(row[18])))
					LoudnessmeanFallingSlope.append(int(float(row[19]))); LoudnessstddevFallingSlope.append(int(float(row[20])))
					SpectralFluxmean.append(int(float(row[21]))); SpectralFluxstddev.append(int(float(row[22])))
					Mfcc1mean.append(int(float(row[23]))); Mfcc1stddevNorm.append(int(float(row[24])))
					Mfcc2mean.append(int(float(row[25]))); Mfcc2stddevNorm.append(int(float(row[26])))
					Mfcc3mean.append(int(float(row[27]))); Mfcc3stddevNorm.append(int(float(row[28])))
					Mfcc4mean.append(int(float(row[29]))); Mfcc4stddevNorm.append(int(float(row[30])))
					JitterLocalmean.append(int(float(row[31]))); JitterLocalstddev.append(int(float(row[32])))
					ShimmerLocalmean.append(int(float(row[33]))); ShimmerLocalstddev.append(int(float(row[34])))
					HNRmean.append(int(float(row[35]))); HNRstddev.append(int(float(row[36])))
					LogRelF0H1H2mean.append(int(float(row[37]))); LogRelF0H1H2stddev.append(int(float(row[38])))
					F1frequencymean.append(int(float(row[39]))); F1frequencystddev.append(int(float(row[40])))
					F1bandwidthmean.append(int(float(row[41]))); F1bandwidthstddev.append(int(float(row[42])))
					F1amplitudeLogRelF0mean.append(int(float(row[43]))); F1amplitudeLogRelF0stddev.append(int(float(row[44])))
					F2frequencymean.append(int(float(row[45]))); F2frequencystddev.append(int(float(row[46])))
					F2bandwidthmean.append(int(float(row[47]))); F2bandwidthstddev.append(int(float(row[48])))
					F2amplitudeLogRelF0mean.append(int(float(row[49]))); F2amplitudeLogRelF0stddev.append(int(float(row[50])))
					F3frequencymean.append(int(float(row[51]))); F3frequencystddev.append(int(float(row[52])))
					F3bandwidthmean.append(int(float(row[53]))); F3bandwidthstddev.append(int(float(row[54])))
					F3amplitudeLogRelF0mean.append(int(float(row[55]))); F3amplitudeLogRelF0stddev.append(int(float(row[56])))
					AlphaRatioVmean.append(int(float(row[57]))); AlphaRatioVstddev.append(int(float(row[58])))
					HammarbergIndexVmean.append(int(float(row[59]))); HammarbergIndexstddev.append(int(float(row[60])))
					SlopeV0_500mean.append(int(float(row[61]))); SlopeV0_500stddev.append(int(float(row[62])))
					SlopeV500_1500mean.append(int(float(row[63]))); SlopeV500_1500stddev.append(int(float(row[64])))
					SpectralFluxVmean.append(int(float(row[65]))); SpectralFluxVstddev.append(int(float(row[66])))
					Mfcc1Vmean.append(int(float(row[67]))); Mfcc1Vstddev.append(int(float(row[68])))
					Mfcc2Vmean.append(int(float(row[69]))); Mfcc2Vstddev.append(int(float(row[70]))); Mfcc3Vmean.append(int(float(row[71])))
					Mfcc3Vstddev.append(int(float(row[72]))); Mfcc4Vmean.append(int(float(row[73]))); Mfcc4Vstddev.append(int(float(row[74])))
					
	return F0semitoneamean, F0semitonestddevNorm, F0semitonepercentile20, F0semitonepercentile50, F0semitonepercentile80, F0semitonepctlrange0_2, F0semitonemeanRisingSlope, F0semitonestddevRisingSlope, F0semitonemeanFallingSlope, F0semitonestddevFallingSlope, Loudnessamean, LoudnessstddevNorm, Loudnesspercentile20, Loudnesspercentile50, Loudnesspercentile80, Loudnesspctlrange0_2, LoudnessmeanRisingSlope, LoudnessstddevRisingSlope, LoudnessmeanFallingSlope, LoudnessstddevFallingSlope, SpectralFluxmean, SpectralFluxstddev, Mfcc1mean, Mfcc1stddevNorm, Mfcc2mean, Mfcc2stddevNorm, Mfcc3mean, Mfcc3stddevNorm, Mfcc4mean, Mfcc4stddevNorm, JitterLocalmean, JitterLocalstddev, ShimmerLocalmean, ShimmerLocalstddev, HNRmean, HNRstddev, LogRelF0H1H2mean, LogRelF0H1H2stddev, LogRelF0H1A3mean, LogRelF0H1A3stddev, F1frequencymean, F1frequencystddev, F1bandwidthmean, F1bandwidthstddev, F1amplitudeLogRelF0mean, F1amplitudeLogRelF0stddev, F2frequencymean, F2frequencystddev, F2bandwidthmean, F2bandwidthstddev, F2amplitudeLogRelF0mean, F2amplitudeLogRelF0stddev, F3frequencymean, F3frequencystddev, F3bandwidthmean, F3bandwidthstddev, F3amplitudeLogRelF0mean, F3amplitudeLogRelF0stddev, AlphaRatioVmean, AlphaRatioVstddev, HammarbergIndexVmean, HammarbergIndexstddev, SlopeV0_500mean, SlopeV0_500stddev, SlopeV500_1500mean, SlopeV500_1500stddev, SpectralFluxVmean, SpectralFluxVstddev, Mfcc1Vmean, Mfcc1Vstddev, Mfcc2Vmean, Mfcc2Vstddev, Mfcc3Vmean, Mfcc3Vstddev, Mfcc4Vmean, Mfcc4Vstddev

					
				
					
								
						
				
					
