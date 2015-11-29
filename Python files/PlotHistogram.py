__author__ = 'Euan Cockburn'
'speech personality project'
'File to plot histogram'

import matplotlib.pyplot as plt

# Plot a histogram
def plotHistogram(Data, Title, Scale):
	plt.hist(Data, bins = 150)
	plt.title(Title)
	plt.xlabel(Scale)
	plt.ylabel("Frequency")
	plt.savefig("/home/euan/Documents/Speech_personality/speech_personality/Plots/" + Title +".png")
