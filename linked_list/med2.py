### AUG 23, 2025 -- P2: ADD TWO NUMBERS ###

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # CARRY-BASED SOLUTION
        dummy = ListNode()
        tail = dummy
        p, q, carry = l1, l2, 0
        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            s = x + y + carry
            carry = s // 10
            tail.next = ListNode(s % 10)
            tail = tail.next
            p = p.next if p else None
            q = q.next if q else None
        return dummy.next
        # INITIAL STRAIGHTFORWARD SOLUTION
        # n1 = pos = 0
        # curr = l1
        # while curr:
        #     n1 += (10**pos) * curr.val
        #     pos += 1
        #     curr = curr.next
        # n2 = pos = 0
        # curr = l2
        # while curr:
        #     n2 += (10**pos) * curr.val
        #     pos += 1
        #     curr = curr.next
        # s = n1 + n2
        # # take num -> split into digits -> reverse
        # target = [int(d) for d in str(s)][::-1]
        # l3head = ListNode()
        # curr = l3head
        # for i in range(len(target)):
        #     curr.val = target[i]
        #     if i+1 < len(target): # if not last
        #         curr.next = ListNode()
        #     curr = curr.next
        # return l3head
