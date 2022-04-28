# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = None
        carry = 0
        r = None
        while (l1 and l2):
            val = l1.val + l2.val
            if carry == 1:
                val += carry

            if val > 9:
                val = val%10
                carry = 1
            else:
                carry = 0

            n = ListNode(val)
            if head == None:
                head = n
            else:
                r.next = n
            
            r = n

            l1 = l1.next
            l2 = l2.next

        if not l1:
            while (l2):
                val = l2.val + carry

                if val > 9:
                    val = val%10
                    carry = 1
                else:
                    carry = 0

                r.next = ListNode(val)
                r = r.next
                l2 = l2.next

        if not l2:
            while (l1):
                val = l1.val + carry

                if val > 9:
                    val = val%10
                    carry = 1
                else:
                    carry = 0

                r.next = ListNode(val)
                r = r.next
                l1 = l1.next

        if carry == 1:
            r.next = ListNode(1)

        return head

