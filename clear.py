# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        currentNode = head
        lastUniqueVal = head.val
        # lastUniqueNode = ListNode(head.val)
        lastUniqueNode = head
        while True :
            currentVal = currentNode.val
            currentNext = currentNode.next
            if lastUniqueVal != currentVal:
                lastUniqueVal = currentVal
                lastUniqueNode.next = currentNode
                lastUniqueNode = currentNode
                
            currentNode = currentNode.next
            if not currentNode:
                break
        if lastUniqueNode.next:
            lastUniqueNode.next = None
        return head
l3 = ListNode(2, None)
l2 = ListNode(2,l3)
l1 = ListNode(1,l2)
l0 = ListNode(1,l1)

sol = Solution()
sol.deleteDuplicates(l0)