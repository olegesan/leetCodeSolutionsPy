class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# l5 = ListNode(5, None)
# l4 = ListNode(5,l5)
# l3 = ListNode(3,l4)
# l2 = ListNode(3,l3)
l1 = ListNode(1,None)
l0 = ListNode(1,l1)
def deleteDuplicates( head: ListNode) -> ListNode:
        # behind = head
        # prevVal = None 
        # times = 0
        # lastUniqueNode = None
        # while head and behind.next:
            
        #     if behind.val == prevVal:
        #         behind.val = behind.next.val
        #         behind.next = behind.next.next
        #     elif behind.val == behind.next.val:
        #         prevVal = behind.next.val
        #         behind.val = behind.next.val
        #         behind.next = behind.next.next
        #     else:
        #         lastUniqueNode = behind
        #         behind = behind.next
        # if prevVal == behind.val:
        #     lastUniqueNode.next = None
        behind = head
        prevVal = None 
        times = 0
        lastUniqueNode = None
        if head:
            while behind.next:

                if behind.val == prevVal:
                    behind.val = behind.next.val
                    behind.next = behind.next.next
                elif behind.val == behind.next.val:
                    prevVal = behind.next.val
                    behind.val = behind.next.val
                    behind.next = behind.next.next
                else:
                    lastUniqueNode = behind
                    behind = behind.next
            # if not lastUniqueNode:
            #     return None
            if prevVal == behind.val:
                if lastUniqueNode:
                    lastUniqueNode.next = None
                else:
                    return None
        return head

            # if behind.val == prevVal:
            #     behind.val = behind.next.val
            #     behind.next = behind.next.next
            #     prevVal = behind.val
            # elif behind.next.val == behind.val:
            #     prevVal = behind.next.val
            #     behind.next = behind.next.next
            #     behind.val = behind.next.val
            #     continue
            # else:
            #     prevVal = behind.val
            # behind = behind.next
            # elif behind.val == behind.next.val:
            #     tempVal = behind.next.val
            #     behind.next = behind.next.next
            # behind = behind.next
            
                
        return head

deleteDuplicates(l0)