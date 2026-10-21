class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        output = []
        for num in nums1:
            if (num in nums2 or num in nums3) and num not in output:
                output.append(num)
        for num in nums2:
            if num in nums3 and num not in output:
                output.append(num)
        return output