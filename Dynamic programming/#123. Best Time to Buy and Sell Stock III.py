#123. Best Time to Buy and Sell Stock III

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=float('Inf')
        
        length=len(prices)
        if length==0:
            return 0
        arr=[0]*length
        arr2=[0]*length
        for i in range(length):
            min1=min(prices[i],min1)
            if prices[i]>min1:
                arr[i]=max(prices[i]-min1,arr[i-1])
            else:
                if i!=0:
                    arr[i]=arr[i-1]
        max1=-float('Inf')
        for i in range(length-1,-1,-1):
            max1=max(prices[i],max1)
            if prices[i]<max1:
                arr2[i]=max(max1-prices[i],arr2[i+1])
            else:
                if i!=length-1:
                    arr2[i]=arr2[i+1]
        output=0
        for i in range(length-1):
            output=max(output,arr[i]+arr2[i+1])
        
        output=max(output,arr[length-1])
        return output