import numpy as np
import cv2
from collections import Counter
from itertools import groupby
import matplotlib.pyplot as plt

def centroid_histogram(lables):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(lables)) + 1)
	(hist, _) = np.histogram(lables, bins = numLabels)
 
	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()
 
	# return the histogram
	return hist

def pixelCount(lables, centers):
    numLabels = np.arange(0, len(np.unique(lables)) + 1)
    unique, counts = np.unique(lables, return_counts=True)

    return list(map(list,zip(centers,counts)))

def plot_colors(hist, centroids):
	# initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0
 
	# loop over the percentage of each cluster and the color of
	# each cluster
	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX
	
	# return the bar chart
	return bar

def get_dominant_colors(gaze):
    
    #3 Channel
    Z = gaze.reshape((-1, 3))

    #convert to np,float32
    Z = np.float32(Z)

    #defome criteria and number of clusters(k)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 16 #Number of colors (Cluster)

    #apply Kmeans
    compactness,labels,centers = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    #Convert back into uint8
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    res2 = res.reshape((gaze.shape))

    #Count how many times a color occurs
    hist = centroid_histogram(labels)
    #print ("Centers")
    #print(centers)

    bar = plot_colors(hist, centers)

    #To display it with matplotlib
    bar = cv2.cvtColor(bar, cv2.COLOR_BGR2RGB)

    # show our color bart
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

    #Show image
    cv2.imshow('gaze',gaze)
    cv2.imshow('res',res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Centers to RGB
    rgb_centers = []
    for center in centers:
        rgb = [center[2],center[1],center[0]]
        rgb_centers.append(rgb)
    return labels, rgb_centers