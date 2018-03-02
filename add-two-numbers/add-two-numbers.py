# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        head = ListNode(None)
        p = head

        while True:

            if l1:
                a = l1.val
            else:
                a = 0

            if l2:
                b = l2.val
            else:
                b = 0

            r = a + b + carry

            if r > 9:
                carry = r // 10
                r = r % 10
            else:
                carry = 0

            p.val = r

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if not l1 and not l2 and carry == 0:
                break

            # New Node
            n = ListNode(None)
            p.next = n
            p = n


        return head

a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c

x = ListNode(5)
y = ListNode(6)
z = ListNode(4)

x.next = y
y.next = z

A = Solution()


s= A.addTwoNumbers(a, x)

print 'Done.'

while True:
    print s.val
    if not s.next:
        break
    s = s.next


a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

x = ListNode(5)
y = ListNode(6)
z = ListNode(4)

x.next = y
y.next = z

A = Solution()


s= A.addTwoNumbers(a, x)

print 'Done.'

while True:
    print s.val
    if not s.next:
        break
    s = s.next


a = ListNode(9)
b = ListNode(9)
c = ListNode(9)

a.next = b
b.next = c

x = ListNode(9)
y = ListNode(9)
z = ListNode(9)

x.next = y
y.next = z

A = Solution()


s= A.addTwoNumbers(a, x)

print 'Done.'

while True:
    print s.val
    if not s.next:
        break
    s = s.next