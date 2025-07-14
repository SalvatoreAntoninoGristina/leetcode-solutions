import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from typing import Optional
from utils.listnode import ListNode

# si puo' fare in una singola passata senza stack perche'
# result = result * 2 + bit
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        stack = []
        
        while head:
            stack.append(head.val)
            head = head.next
        i = 0
        sum = 0
        while stack:
            sum = sum + (stack.pop() * 2**i)
            i+=1
        
        return sum
    

l1 = ListNode(1, ListNode(0, ListNode(1)))

a = Solution().getDecimalValue(l1)
print(a)
