[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> What percentage of the U.S. malepopulation is in this range (5'10" to 6'1")?
>> By using the dist.cdf() function presented in this chapter, we can enter the height of an individual in centimeters and it will return a value representing the percentile in which that individual falls. In this problem, we can translate the given ranges to 177.8cm to 185.4cm.  
>>In python our code would read: """low = dist.cdf(177.8)    # 5'10"  
                                 high = dist.cdf(185.4)   # 6'1"
                                 low, high, high-low"""         
The output returned for the difference is .342, meaning that about 34.2% of U.S. adult males fall into this range according to our data.
