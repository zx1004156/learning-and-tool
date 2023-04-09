from typing import List

arr = [1,0,2,3,0,4,5,0]


class Solution:
    def duplicateZeros(self, arr1: List[int]) -> None:
        #在我要的變數後面加上 :型別，型別的第一個字要大寫，最上面引入時要寫 from typing import List
    #def duplicateZeros(self, arr1):    
        i = 0
        n = len(arr)
        while i<n:
            #print(arr)
            #print(i)
            if(arr[i]==0):
                arr[i+1:n] = arr[i:n-1] 
                i+=2
            else:
                i+=1
        return [number for number in arr1]

s = Solution()
arr2 = s.duplicateZeros(arr)
print(arr2)


########################################################
