#Сложность данного алгоритма O(n)
#Для реализации алгоритма используется обход в глубину, также используется очередь
#мы проходимся по дереву и сохраняем значения ячеек
#после чего делим сумму всех ячеек на их количество.


class TreeNode:
    def init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        if not root:
            return None
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            s = 0
            for _ in range(size):
                node = queue.pop(0)
                s+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(s/size)
        return res