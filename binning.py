import matplotlib.pyplot as plt
import numpy as np

def Smoother(d : list, depth : int):
    smoothened = []
    sum = 0.0
    i = 0
    while i < len(d):
        sum += d[i]
        if (i+1) % depth == 0:
            smoothened.append(sum / depth)
            sum = 0.0
        i += 1
    return smoothened

def EqFreqBins(d : list, num_bins : int):
    bins = []
    size = len(d) / num_bins
    for i in range(len(d)):
        if (i+1) % size == 0:
            bins.append(d[i])
    return bins

def equalObs(x, nbin):
    nlen = len(x)
    return np.interp(np.linspace(0, nlen, nbin + 1), np.arange(nlen), np.sort(x))

data = [13,15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,35,36,40,45,46,52,70]
NUM_BINS = 9
figure, axis = plt.subplots(2,2)
axis[0, 0].hist(data, edgecolor = 'black')                                      # Unsmoothened
axis[0, 0].set_title("Unsmoothened Data")
axis[1, 0].hist(Smoother(data, 3), edgecolor = 'black')                         # Smoothened
axis[1, 0].set_title("Smoothened Data")
axis[0, 1].hist(data, edgecolor = 'black', bins=NUM_BINS)                       # Equal Width
axis[0, 1].set_title("Equal Width Binning")
axis[1, 1].hist(data, edgecolor='black', bins=equalObs(data, NUM_BINS))         # Equal 
axis[1, 1].set_title("Equal Frequency Binning")
plt.show()