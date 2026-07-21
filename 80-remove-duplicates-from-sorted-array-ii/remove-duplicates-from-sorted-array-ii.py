class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1

        k=0
        for a,b in sorted(freq.items()):
            if b>=2:
                nums[k]=a
                nums[k+1]=a
                k+=2
            else:
                nums[k]=a
                k+=1

        return k
            
                

        