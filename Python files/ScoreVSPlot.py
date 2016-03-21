__author__ = 'Euan Cockburn'
'speech personality project'
'file for mapping feature against score'

import matplotlib.pyplot as plt
import numpy as np

def ScoreVSplot(Score, Feature, Data):
	
	# For this corpus meta data willl only ever be split into two
	option_1 = []
	option_2 = []
	
	values = []

	# For each entry in the Data list
	for i in xrange(len(Data)):
		# Determine where the data of the feature being examined is to be stored based on the score value
		values.append(Data[i][Score])

	# Determine the median value
	median_value = np.median(values)

	# Split the data into two lists based on where the median lies

	for i in xrange(len(Data)):
		if Data[i][Score] > median_value:
			option_1.append(Data[i][Feature])
		elif Data[i][Score] <= median_value:
			option_2.append(Data[i][Feature])

	plt.figure()
	plt.hist(option_1, bins=len(option_1)/10)
	plt.hist(option_2, bins=len(option_2)/10)
	plt.legend([Score + " Upper", Score + " Lower"])
	plt.xlabel(Feature)
	plt.ylabel('occurances')
	plt.savefig("/home/euan/Documents/university/year4/speech_personality/Plots/VSPlots/" + Feature + "_" + Score + "_Hist" + ".png")

	#plt.figure()
	#i = 0
	#for i in xrange(len(Data)):
#		plt.plot(Data[i][Score], Data[i][Feature], 'bx')
#
#	plt.xlabel(Score)
#	plt.ylabel(Feature)
#	plt.savefig("/home/euan/Documents/university/year4/speech_personality/Plots/VSPlots/" + Feature + "_" + Score + "_Scatter" + ".png")
#	
#	plt.close("all")
