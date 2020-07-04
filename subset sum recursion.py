def subset(input,sum,n):


    if sum is 0:
        return True
    
    if n is 0:
        return False
    
    if input[n-1] > sum:
        return subset(input,sum,n-1)
    
    else:
        return ( subset(input,sum,n-1) or subset(input,sum-input[n-1],n-1) )
        




input= [3, 34, 4, 12, 5, 2]
sum = 100

x= subset(input,sum,len(input))
print(x)
