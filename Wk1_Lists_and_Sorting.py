import math
from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
        right = len(numbers)-1
        left = 0
        while left != right:
            if numbers[left]+numbers[right] > target:
                right-=1
            elif numbers[left]+numbers[right] < target:
                left+=1
            elif numbers[left]+numbers[right] == target:
                return [left+1, right+1]
            else:
                break

def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

def productExceptSelf(nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

#print(twoSum([2,7,11,15], 9))