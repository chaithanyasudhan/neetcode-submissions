class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = set(nums)
        s = 0

        for i in n:
            # Only process if 'i' is the START of a sequence
            if i - 1 not in n:
                length = 1
                while (i + length) in n:
                    length += 1
                if length > s:
                    s = length

        return s