#第一种方法就是排序＋双指针
from typing import List
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        n = len(nums)
        nums.sort()
        l = 0
        r = len(nums)-1
        while(l<r):
            if(nums[i]+nums[r]==target):
                return [l,r]
            elif(nums[i]+nums[r]<target):
                i+=1
            else:
                r-+1
        return []

#第二种方法用哈希表降低时间复杂度（开阔思路！！） 每次遍历都用target-nums[i]，如果没有遇到过就存进去，以此类推，遇到过就输出。
class Solution1:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        n = len(nums)
        mapper=[]
        for i in range(n):
            if(target-nums[i] in mapper):
                return[mapper[target-nums[i]],i]
            else:
                mapper[nums[i]]=i
        return []