[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

 Exercise 7.1 Using data from the NSFG, make a scatter plot of birth weight versus 
 mother’s age. Plot percentiles of birth weight versus mother’s age. Compute Pearson’s 
 and Spearman’s correlations. How would you characterize the relationship between 
 these variables?

import nsfg
import thinkplot
import numpy as np

df = nsfg.ReadFemPreg()

##Make & show scatterplot
thinkplot.Scatter(df['agepreg'],df['totalwgt_lb'],alpha=1.0)
thinkplot.Config(xlabel='age (years)',
                     ylabel='weight (lbs)',
                     xlim=[10, 45],
                     ylim=[0, 15],
                     legend=False)
thinkplot.show()


#drop any row with NA in either agepreg or totalwgt_ln
df2=df.dropna(subset=['agepreg','totalwgt_lb'])

#create a np array with numbers from 10(minage)-48(maxage:44) in increments of 3 
#and not including 48
bins = np.arange(10, 48, 3)

#can't yet figure out what this does
indices = np.digitize(df2.agepreg, bins)


"""
    ages = [group.agepreg.mean() for i, group in groups][1:-1]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups][1:-1]

    thinkplot.PrePlot(3)
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Save(root='chap07scatter3',
                   formats=['jpg'],
                   xlabel="mother's age (years)",
                   ylabel='birth weight (lbs)')
"""
