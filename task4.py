#Сложность алгоритма O(n)
#Проходимся по односвязному списку и сохраняем значения ячеек
#затем перевод их в двоичную систему счисления


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head):
        s = ''
        while head:
            s += str(head.val)
            head = head.next
        return int(s, 2)
