[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import random
import thinkplot
import thinkstats2
import cumulative

t = [random.random() for x in range(1000)]
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth = 0.1)
thinkplot.show()


cdf = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf)
thinkplot.show()

## This cumulative distribution function is uniformly distributed. Once the randomly generated 1000 numbers between 0 and 1  are sorted, you can see that .5 values fall within the 50th percentile, .25 fall within the 25th percentile, and so on.
