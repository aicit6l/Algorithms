class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []

        for i in range(len(nums)):  # for each element
            for n in range(i+1, len(nums)):  # iterate through every other element
                if nums[i] + nums[n] == target: 
                    result.append(i)
                    result.append(n)
                    return result
        



# Test Cases
SumOfTwoA: Solution = Solution.twoSum(Solution.twoSum, [2, 7, 11, 15], 9)
SumOfTwoB: Solution = Solution.twoSum(Solution.twoSum, [3,3], 6)
SumOfTwoC: Solution = Solution.twoSum(Solution.twoSum, [3,2,4], 6)
SumOfTwoD: Solution = Solution.twoSum(Solution.twoSum, [2,7,11,13,15,23], 26)
SumOfTwoE: Solution = Solution.twoSum(Solution.twoSum, [2, 7, 11, 15], 17)

print(f"First Test Case Output : {SumOfTwoA}")
print(f"Second Test Case Output : {SumOfTwoB}")
print(f"Third Test Case Output : {SumOfTwoC}")
print(f"Fourth Test Case Output : {SumOfTwoD}")
print(f"Fifth Test Case Output : {SumOfTwoE}")