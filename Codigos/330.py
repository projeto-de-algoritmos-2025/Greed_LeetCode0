class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1        # menor número que ainda não conseguimos formar
        i = 0           # índice em nums
        patches = 0     # número de valores adicionados

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # patchar com 'miss' porque não há número em nums que o cubra
                miss += miss
                patches += 1

        return patches
    