[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Exercise 2.4 Using the variable totalwgt_lb, investigate whether first ba- bies 
are lighter or heavier than others. Compute Cohen’s d to quantify the difference 
between the groups. How does it compare to the difference in pregnancy length?

import nsfg as nsfg
import thinkstats2 as code


preg = nsfg.ReadFemPreg()
nsfg.CleanFemPreg(preg)
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
code.CohenEffectSize(firsts['totalwgt_lb'], others['totalwgt_lb'])
##returns -0.088672927072602

>>> firsts.mean()['totalwgt_lb']
7.201094430437772
>>> others.mean()['totalwgt_lb']
7.3258556149732623

Looking at only means, it appears that first born babies have a total birth weight that
is less than babies born in other orders. Looking at the effect size, it appears that
the difference is .09 standard deviations, or 1/10th of a standard deviation. 
