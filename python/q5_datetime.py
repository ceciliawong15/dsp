# Hint:  use Google to find python function

####a) 
from datetime import datetime
date_start = '01-02-2013'  
date_stop = '07-28-2015'  

date_start = datetime.strptime(date_start, "%m-%d-%Y")
date_stop = datetime.strptime(date_stop, "%m-%d-%Y")

print "Final Answer to A.:", abs((date_stop-date_start).days)

####b)  
from datetime import datetime
date_start = '12312013'  
date_stop = '05282015'  

date_start = datetime.strptime(date_start, "%m%d%Y")
date_stop = datetime.strptime(date_stop, "%m%d%Y")

print "Final Answer to B.:", abs((date_stop-date_start).days)

####c)  
from datetime import datetime
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

ate_start = datetime.strptime(date_start, "%d-%b-%Y")
date_stop = datetime.strptime(date_stop, "%d-%b-%Y")

print "Final Answer C.:", abs((date_stop-date_start).days
