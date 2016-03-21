__author__ = 'Euan Cockburn'
'speech personality project'
'file for mapping feature against meta'

import matplotlib.pyplot as plt

def MetaVSplot(Meta, Feature, Data):

	# For this corpus meta data willl only ever be split into two
	option_1 = ""
	option_2 = ""

	# Determine what meta data is being used for split.
	if Meta == 'Gender':
		option_1 = "F"
		option_2 = "M"
	else:
		option_1 = "J"
		option_2 = "G"
	

	option_1_set = []
	option_2_set = []

	# For each entry in the Data list
	for i in xrange(len(Data)):
		# Determine where the data of the feature being examined is to be stored based on the meta value
		if Data[i][Meta] == option_1:
			option_1_set.append(Data[i][Feature])
		else:
			option_2_set.append(Data[i][Feature])

	plt.figure()
	plt.hist(option_1_set, bins=len(option_1_set)/10)
	plt.hist(option_2_set, bins=len(option_2_set)/10)
	plt.legend([option_1, option_2])
	plt.xlabel(Feature)
	plt.ylabel('occurances')
	plt.savefig("/home/euan/Documents/university/year4/speech_personality/Plots/VSPlots/" + Feature + "_" + Meta + "_Hist" + ".png")

	plt.figure()
	i = 0
	for i in xrange(len(Data)):
		if Data[i][Meta] == option_1:
			plt.plot(i, Data[i][Feature], 'bx')
		else:
			plt.plot(i, Data[i][Feature], 'ro')
	
	plt.xlabel('Index')
	plt.ylabel(Feature)
	plt.savefig("/home/euan/Documents/university/year4/speech_personality/Plots/VSPlots/" + Feature + "_" + Meta + "_Scatter" + ".png")
	
	plt.close("all")
