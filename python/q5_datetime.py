# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'     
  
from datetime import datetime  
date_format = "%m-%d-%Y"  
date_start =  datetime.strptime('01-02-2013', date_format)  
date_stop = datetime.strptime('07-28-2015', date_format)  
delta = date_start - date_stop  
print(abs(delta.days)) # that's it

####b)  
date_start = '12312013'  
date_stop = '05282015'  
  
from datetime import datetime   
date_format = "%m%d%Y"  
date_start =  datetime.strptime('12312013', date_format)  
date_stop = datetime.strptime('05282015', date_format)  
delta = date_start - date_stop  
print(abs(delta.days)) # that's it

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
from datetime import datetime  
date_format = "%d-%b-%Y"  
date_start =  datetime.strptime('15-Jan-1994', date_format)  
date_stop = datetime.strptime('14-Jul-2015', date_format)  
delta = date_start - date_stop  
print(abs(delta.days)) # that's it

