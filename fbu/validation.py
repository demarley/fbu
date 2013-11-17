import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from numpy import mean,std,arange

def plot(dirname,data,bkgd,resmat,trace,lower=[],upper=[]):
    import os
    if not os.path.exists(dirname+'_monitoring'):
        os.makedirs(dirname+'_monitoring')
    nbins = len(data)
    bintrace = trace
    for bin in xrange(nbins): 
        ax = plt.subplot(211)
        xx = bintrace[bin]
        mu = mean(xx)
        sigma = std(xx)
        n, bins, patches = plt.hist(xx, bins=50, normed=1, facecolor='green', alpha=0.5, histtype='stepfilled')
        yy = mlab.normpdf(bins,mu,sigma)
        plt.plot(bins,yy,'r-')
        plt.ylabel('Probability')
        plt.xlabel('Bin content')
        ymean = mean(ax.get_ylim())
        plt.hlines(ymean,lower[bin],upper[bin],linestyles='dashed',colors='m',label='hyperbox')
        plt.vlines(data[bin],0.,ymean,linestyles='solid',colors='c',label='data')
        plt.xlim(xmin=0)
        plt.subplot(212)
        x = arange(len(bintrace[bin]))
        plt.plot(x,bintrace[bin],label='trace of bin %d'%bin)
        plt.savefig(dirname+'_monitoring/bin%s.eps'%bin)
        plt.close()
