num=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
#sorting with zeroes at end

num.sort()
for i in num:
    if(i==0):
        num.remove(0)
        num.append(0)
print(num)
    
        
        
    
