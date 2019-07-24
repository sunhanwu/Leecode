class Solution:
    # 思路就是暴露寻找
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                idx = nums.index(target - nums[i])
                if idx == i:
                    pass # 注意样例[3,2,4],6中，不能是[0,0],只能是[1,2]，所以需要判断下表是否一致
                else:
                    return [i,nums.index(target - nums[i])]

