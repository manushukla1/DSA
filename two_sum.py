from typing import List
def twoSum( nums,  target) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums [j] == target:
                    return [i, j]
        return []

nums = [2, 7, 11, 15]
print(twoSum(nums,9))

#Solved via brute force approach where i have fixed the first number as i and j as i +1 the next number in the array
# if the sum of i + j is equal to target we return the indexes if not we increase the value of i and j
# means we are checking every index one by one.