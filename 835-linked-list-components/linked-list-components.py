# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        temp=head
        s=set(nums)
        while temp:
            if temp.next and temp.val in nums and temp.next.val not in nums:
                ans+=1
            elif temp.val in nums and not temp.next:
                ans+=1
                break
            temp=temp.next

        return ans 
            
        