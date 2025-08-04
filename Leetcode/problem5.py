#Definition for singly linked list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        list3 = ListNode()
        print(list3)
        head1 = list1.val
        head2 = list2.val
        head3 = None
        i, j = 0

        while(list1.next != None and list2.next !=None):
            if list3.val == 0 and list3.next == None:
                if head1 > head2:
                    list3.val = head2
                    j += 1
                    head2 = list2.next.val
                    list2 = list2.next
                else:
                    list3 = head1
                    i += 1
                    head1 = list1.next.val
                    list1 = list1.next
            else:
                if head1 > head2:
                    list3.val = head2
                    j += 1
                    head2 = list2.next.val
                    list2 = list2.next
                else:
                    list3.val = head1
                    i += 1
                    head1 = list1.next.val
                    list1 = list1.next
            return head3
        

if __name__ == "__main__":
    solution = Solution.mergeTwoLists([1,2,3], [4,5,6])
    