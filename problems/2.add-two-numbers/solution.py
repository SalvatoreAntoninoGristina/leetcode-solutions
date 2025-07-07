
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from typing import Optional
from utils.listnode import ListNode


def addValues(output:ListNode, s:str, c:int, i:int) -> ListNode:
    if (i==c-1):
        output.val = int(s[c-i-1])
        output.next = None
        return output
    

    return ListNode( int(s[c-i-1]), addValues(ListNode(),s,c,i+1))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        rateo = 1
        tmp_sum = 0
        while l1:
            tmp_sum += l1.val * rateo
            rateo *= 10
            l1 = l1.next
        rateo = 1
        tmp_sum2 = 0
        while l2:
            tmp_sum2 += l2.val * rateo
            rateo *= 10
            l2 = l2.next
        
        sum = tmp_sum + tmp_sum2
        s_sum = str(sum)
        count = len(str(sum))
        

        

        return addValues(ListNode(),s_sum,count,i=0) # type: ignore fare ricorsione 





# Lista 1: 1 -> 2 -> 3
l1 = ListNode(1, ListNode(2, ListNode(3)))

# Lista 2: 4 -> 5 -> 6
l2 = ListNode(4, ListNode(5, ListNode(6)))
sol = Solution()
risultato = sol.addTwoNumbers(l1, l2)
while risultato:
    print(risultato.val)
    risultato = risultato.next
