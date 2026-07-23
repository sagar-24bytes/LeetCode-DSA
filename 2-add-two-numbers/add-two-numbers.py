# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1=l1
        temp2=l2
        dummy=ListNode(0)
        curr=dummy
        carry=0
        while temp1 or temp2:
            total=carry
            if temp1:
                total+=temp1.val
            if temp2:
                total+=temp2.val

            carry=total//10
            num=total%10
            new_node= ListNode(num)
            curr.next=new_node
            curr=new_node
            if temp1:
                temp1=temp1.next
            if temp2:
                temp2=temp2.next
        if carry!=0:
            new_node=ListNode(carry)
            curr.next=new_node
            curr=new_node
        return dummy.next

        