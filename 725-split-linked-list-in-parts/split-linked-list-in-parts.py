# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        ans=[]
        def size(node):
            if not node:
                return 0
            count=0
            while node:
                count+=1
                node=node.next
            return count
        s=size(head)
        base=s//k
        extra=s%k
        prev=None
        temp=head
        for i in range(k):
            dummy=temp
            curr_size=base+(1 if i<extra else 0)
            # extra-=1
            x=0
            while temp and x<curr_size:
                x+=1
                prev=temp
                temp=temp.next
                # prev.next=None
            if prev:
                prev.next=None
            ans.append(dummy)
            
        for i in range(k-len(ans)):
            ans.append(None)
        return ans 

        