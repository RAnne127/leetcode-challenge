class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # First element will be the first unique
        count = 1
        unique = nums[0]

        # Check for the second element first
        for i in range(1, len(nums)):
            # Check if the current element is new
            if nums[i] != unique:
                # Update the array of the new unique element
                nums[count] = nums[i]
                unique = nums[count]
                count += 1

        return count