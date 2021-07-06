#2. Add Two Numbers

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        returnVal=pointer=ListNode(0)
        carry=0
        
        while l1 or l2:
            addVal=(l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            carry=0            
            if addVal>=10:
                carry=1
                addVal=addVal%10               
            pointer.next=ListNode(addVal)
            l1=l1.next if l1 else l1
            l2=l2.next if l2 else l2
            pointer=pointer.next
        if carry:
            pointer.next=ListNode(carry)
        return returnVal.next
 
