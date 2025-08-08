# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        length = 0
        dummyHead = head
        while dummyHead != None:
            length = length+1
            dummyHead = dummyHead.next
        
        indexToRemove = length - n
            
        nodeCounter = 0
        tempHead = head
        while nodeCounter != indexToRemove:
            prevNode = tempHead
            tempHead = tempHead.next

        prevNode.next = tempHead.next
    
        return head

if __name__ == "__main__":
    print(Solution().removeNthFromEnd(head=[1,2,3,4,5], n=2))