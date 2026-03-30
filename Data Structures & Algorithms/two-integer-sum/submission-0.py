class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i, num in enumerate(nums):
            answer = target - num
            if answer in prev_map:
                return [prev_map[answer], i]
            prev_map[num] = i




            #for j, num2 in enumerate(nums):
                #if num + num2 == target:
                    #return [i, j]
        

