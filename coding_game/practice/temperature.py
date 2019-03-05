import sys
import math
n = int(input())
tem=[]
tem_abs=[]
for i in input().split(): #get the array 
    t = int(i)
    tem.append(t)
    tem_abs.append(abs(t))
result=[]
for i in tem:           #compare the array 
    if abs(i)==min(tem_abs):
        result.append(i)    #append in the result array 
result.sort()
if len(result)!=0:
    print(result[-1])       #ans will always be at the last index of the list 
else:
    print(0)
