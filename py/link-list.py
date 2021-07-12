class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head):
    def reverse(node):
        nodeNext = None
        while node:
            temp = node.next
            node.next = nodeNext
            nodeNext = node
            node = temp
        return nodeNext


    if head and head.next:
        slow = head
        slowHead = head
        quick = head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next

        quickHead = slow.next
        slow.next = None
        quickHead = reverse(quickHead)
        while (quickHead):
            if quickHead.val != slowHead.val:
                return False
            quickHead = quick.next
            slowHead = slowHead.next
    return True


d = ListNode(1)
c = ListNode(2)
b = ListNode(1)
a = ListNode(1)
a.next = b
b.next = c
c.next = d

print(isPalindrome((a)))


def getIntersectionNode( headA,headB):
    link = headA
    while (link.next):
        link = link.next
    link.next = headB
    slow = headA
    fast = headA
    cur = headA
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            while cur != fast:
                cur = cur.next
                fast = fast.next
            link.next = None
            return cur


nodeA = ListNode(4)
nodeB = ListNode(1)
nodeC = ListNode(8)
nodeD = ListNode(4)
nodeE = ListNode(5)

nodeF = ListNode(5)
nodeG = ListNode(0)
nodeH = ListNode(1)

nodeF.next = nodeG
nodeG.next = nodeH
nodeH.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeA.next = nodeB
nodeB.next = nodeC

getIntersectionNode(nodeF,nodeA)