import numpy as np 
import pandas as pd 
#data
x=[ 31,31,32,32,32,34,35,36,37,38,38,38]
m=6
step1= len(x)*m
step2=step1-np.sum(x) 

x=np.array(x)
q1=np.percentile(x,75) 
q3=np.percentile(x,25)
 #execute
print("this is the interquarter ranch",q3-q1)
print(len(x))
print("this is the sorted nmbers",np.sort(x))
print("This is the standard devistation",np.std(x,ddof=1))
print("this is the number:",step2)
print("this is the median",np.median(x))
print("this is the mean",np.mean(x))
#check
for i in range(len(x)):
    if x[i]==0:
        x[i]=step2
#print(x)
print("this is the check:",np.mean(x))
 