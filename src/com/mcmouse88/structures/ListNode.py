class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = []
        curr = self
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return "".join(res)