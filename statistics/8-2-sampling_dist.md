[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

import estimation as est
est.Estimate3(n=10,m=1000)
"""Experiment 3
rmse L 0.909193736293
rmse Lm 1.18812755941
mean error L 0.270992219007
mean error Lm 0.286422779319
"""

est.Estimate3(n=100,m=1000)
"""Experiment 3
rmse L 0.200385626379
rmse Lm 0.294385399134
mean error L 0.0241733045399
mean error Lm 0.0337605189482
"""
est.Estimate3(n=1000,m=1000)
"""
Experiment 3
rmse L 0.0632477534667
rmse Lm 0.0926622609305
mean error L 0.00321947408127
mean error Lm 0.00532126040188
"""

###The standard error is decreasing as the sample size increases. **How to find the confidence interval??

