def best_time(prices):
    i,j = 0,1
    max_trans=0
    while j<len(prices):
        if prices[i]<prices[j]:
            max_trans =max(max_trans,prices[j]-prices[i])
            
            j=j+1
        else:
            i=j
            j+=1
        
    return max_trans

print(best_time([2,1,2,1,0,1,2]) )       