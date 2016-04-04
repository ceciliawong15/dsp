
import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh)

thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.Show()

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
    
biased = BiasPmf(pmf, label='biased')
    
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()

pmf.Mean()
##returns 1.0242051550438309
biased.Mean()
##returns 2.4036791006642821
