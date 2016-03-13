__author__ = 'Euan Cockburn'
'speech personality project'
'File to plot histogram'

import matplotlib.pyplot as plt

def plotfeatures(features):
	F0semitoneamean = []
	Loudnessamean = []
	SpectralFluxmean = []
	Mfcc1mean = [];	Mfcc2mean = [];	Mfcc3mean = [];	Mfcc4mean = []
	JitterLocalmean = []
	ShimmerLocalmean = []
	HNRmean = []
	LogRelF0H1H2 = []
	LogRelF0H1A3mean = []
	F1frequencymean = []; F1bandwidthmean = []; F1amplitudeLogRelF0mean = []
	F2frequencymean = []; F2bandwidthmean = []; F2amplitudeLogRelF0mean = []
	F3frequencymean = []; F3bandwidthmean = []; F3amplitudeLogRelF0mean = []
	AlphaRatioVmean = []
	HammarbergIndexVmean = []
	SlopeV0_500mean = []; SlopeV500_1500mean = []
	SpectralFluxVmean = []
	Mfcc1Vmean = []; Mfcc2Vmean = []; Mfcc3Vmean = []; Mfcc4Vmean = []
	AlphaRatioUVmean = []; HammarbergIndexUVmean = []
	SlopeUV0_500mean = []; SlopeUV500_1500mean = []
	SpectralFluxUVmean = []; LoudnessPeaksPerSec = []
	VoicedSegmentsPerSec = []; MeanVoicedSegmentLengthSec = []
	MeanUnvoicedSegmentLength = []; EquivalentSoundLevel_dBp = []
	LogRelF0H1H2mean = []

	for entry in features:
		F0semitoneamean.append(entry['F0semitoneamean'])
		Loudnessamean.append(entry['Loudnessamean'])
		SpectralFluxmean.append(entry['SpectralFluxmean'])
		Mfcc1mean.append(entry['Mfcc1mean']); Mfcc2mean.append(entry['Mfcc2mean']); Mfcc3mean.append(entry['Mfcc3mean'])
		Mfcc4mean.append(entry['Mfcc4mean'])
		JitterLocalmean.append(entry['JitterLocalmean']); ShimmerLocalmean.append(entry['ShimmerLocalmean'])
		HNRmean.append(entry['HNRmean']); LogRelF0H1H2mean.append(entry['LogRelF0H1H2mean'])
		LogRelF0H1A3mean.append(entry['LogRelF0H1A3mean'])
		F1frequencymean.append(entry['F1frequencymean']); F1bandwidthmean.append(entry['F1bandwidthmean'])
		F1amplitudeLogRelF0mean.append(entry['F1amplitudeLogRelF0mean'])
		F2frequencymean.append(entry['F2frequencymean']); F2bandwidthmean.append(entry['F2bandwidthmean'])
		F2amplitudeLogRelF0mean.append(entry['F2amplitudeLogRelF0mean'])
		F3frequencymean.append(entry['F3frequencymean']); F3bandwidthmean.append(entry['F3bandwidthmean'])
		F3amplitudeLogRelF0mean.append(entry['F3amplitudeLogRelF0mean'])
		AlphaRatioVmean.append(entry['AlphaRatioVmean'])
		HammarbergIndexVmean.append(entry['HammarbergIndexVmean'])
		SlopeV0_500mean.append(entry['SlopeV0_500mean']); SlopeV500_1500mean.append(entry['SlopeV500_1500mean'])
		SpectralFluxVmean.append(entry['SpectralFluxVmean'])
		Mfcc1Vmean.append(entry['Mfcc1Vmean']); Mfcc2Vmean.append(entry['Mfcc2Vmean']); Mfcc3Vmean.append(entry['Mfcc3Vmean'])
		Mfcc4Vmean.append(entry['Mfcc4Vmean'])
		AlphaRatioUVmean.append(entry['AlphaRatioUVmean']); HammarbergIndexUVmean.append(entry['HammarbergIndexUVmean'])
		SlopeUV0_500mean.append(entry['SlopeUV0-500mean']); SlopeUV500_1500mean.append(entry['SlopeUV500-1500mean'])
		SpectralFluxUVmean.append(entry['SpectralFluxUVmean']); LoudnessPeaksPerSec.append(entry['LoudnessPeaksPerSec'])
		VoicedSegmentsPerSec.append(entry['VoicedSegmentsPerSec'])
		MeanVoicedSegmentLengthSec.append(entry['MeanVoicedSegmentLengthSec'])
		MeanUnvoicedSegmentLength.append(entry['MeanUnvoicedSegmentLength'])
		EquivalentSoundLevel_dBp.append(entry['EquivalentSoundLevel_dBp'])
		
	plotHistogram(F0semitoneamean, "Average Fundamental frequency", "Hz")
	plotHistogram(Loudnessamean, "Average Loudness", "")
	plotHistogram(SpectralFluxmean, "Average Spectral Flux", "")
	plotHistogram(Mfcc1mean, "Average mfcc1", ""); plotHistogram(Mfcc2mean, "Average mfcc2", "")
	plotHistogram(Mfcc3mean, "Average mfcc3", ""); plotHistogram(Mfcc4mean, "Average mfcc4", "")
	plotHistogram(JitterLocalmean, "Average Local jitter", "")
	plotHistogram(ShimmerLocalmean, "Average Local shimmer", "")
	plotHistogram(HNRmean, "Mean Harmonic Noise Ratio", "")
	plotHistogram(LogRelF0H1H2mean, "LogRelF0H1H2", ""); plotHistogram(LogRelF0H1A3mean, "LogRelFOH1A3", "")
	plotHistogram(F1frequencymean, "Average Formant 1 Frequency", ""); plotHistogram(F1bandwidthmean, "Average Formant 1 Bandwidth", "")
	plotHistogram(F1amplitudeLogRelF0mean, "Average Formant 1 Amplitude Frequency LogRel", "")
	plotHistogram(F2frequencymean, "Average Formant 2 Frequency", ""); plotHistogram(F2bandwidthmean, "Average Formant 2 Bandwidth", "")
	plotHistogram(F2amplitudeLogRelF0mean, "Average Formant 2 Amplitude Frequency LogRel", "")
	plotHistogram(F3frequencymean, "Average Formant 3 Frequency", ""); plotHistogram(F3bandwidthmean, "Average Formant 3 Bandwidth", "")
	plotHistogram(F3amplitudeLogRelF0mean, "Average Format 3 Amplitude Frequency LogRel", "")
	plotHistogram(AlphaRatioVmean, "Average Alpha Ratio", "")
	plotHistogram(HammarbergIndexVmean, "Average Hammarberg Index", "")
	plotHistogram(SlopeV0_500mean, "Average slope from 0 to 500", "")
	plotHistogram(SlopeV500_1500mean, "Average slope from 500 to 1500", "")
	plotHistogram(SpectralFluxVmean, "Average spectral flux V", "")
	plotHistogram(Mfcc1Vmean, "Average mfcc1V", ""); plotHistogram(Mfcc2Vmean, "Average mfcc2V", "")
	plotHistogram(Mfcc3Vmean, "Average mfcc3V", ""); plotHistogram(Mfcc4Vmean, "Average mfcc4V", "")
	plotHistogram(AlphaRatioUVmean, "Average UV AlphaRatio", "")
	plotHistogram(HammarbergIndexUVmean, "Average UV Hammarberg Index", "")
	plotHistogram(SlopeUV0_500mean, "Average UV slope from 0 to 500", "")
	plotHistogram(SlopeUV500_1500mean, "Average UV slope from 500 to 1500", "")
	plotHistogram(SpectralFluxUVmean, "Average UV Spectral Flux", "")
	plotHistogram(LoudnessPeaksPerSec, "Loudnes Peaks per second", "Pps")
	plotHistogram(VoicedSegmentsPerSec, "Voiced Segments per second", "VSps")
	plotHistogram(MeanVoicedSegmentLengthSec, "Voiced segments average duration", "s")
	plotHistogram(MeanUnvoicedSegmentLength, "Unvoiced segments average duration", "s")
	plotHistogram(EquivalentSoundLevel_dBp, "Equivalent Sound Level", "dBp")
	
	
# Plot a histogram
def plotHistogram(Data, Title, Scale):
	plt.figure()
	plt.hist(Data, bins = 64, label = Title)
	plt.legend(loc='upper right')
	plt.title(Title)
	plt.xlabel(Scale)
	plt.ylabel("Frequency")
	plt.savefig("/home/euan/Documents/university/year4/speech_personality/Plots/" + Title +".png")
	plt.close("all")
