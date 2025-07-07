# Documentation for solution.py

## Overview
This script implements a solution to the LeetCode problem "Add Two Numbers" using singly-linked lists. The script defines a `ListNode` class for the linked list nodes, a recursive helper function to build the result list, and a `Solution` class with the main logic. At the end, it demonstrates usage with two example lists.

## Components

### 1. ListNode Class
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
Represents a node in a singly-linked list, with an integer value and a reference to the next node.

### 2. addValues Function
```python
def addValues(output: ListNode, s: str, c: int, i: int) -> ListNode:
    if (i == c-1):
        output.val = int(s[c-i-1])
        output.next = None
        return output
    return ListNode(int(s[c-i-1]), addValues(ListNode(), s, c, i+1))
```
A recursive function that builds a linked list from a string of digits, placing each digit in a node in reverse order (to match the LeetCode problem's requirements).

### 3. Solution Class
```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ...
```
Implements the main logic:
- Converts both input linked lists to integers (assuming least-significant digit comes first).
- Sums the two integers.
- Converts the sum back to a linked list using `addValues`.

### 4. Example Usage
```python
# Lista 1: 1 -> 2 -> 3
l1 = ListNode(1, ListNode(2, ListNode(3)))
# Lista 2: 4 -> 5 -> 6
l2 = ListNode(4, ListNode(5, ListNode(6)))
sol = Solution()
risultato = sol.addTwoNumbers(l1, l2)
while risultato:
    print(risultato.val)
    risultato = risultato.next
```
Creates two example lists, adds them, and prints the result node by node.

## Notes
- The script assumes the input lists represent numbers in reverse order (as per LeetCode's convention).
- The recursive approach in `addValues` builds the result list from the sum's string representation.
- The code is written in Python and uses type hints for clarity.
