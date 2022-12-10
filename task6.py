#Сложность алгоритма O(n)
#реализуется с помощью обхода в глубину
#находим диаметр дерева

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def dfs(root):
            if not root: 
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.ans = max(self.ans, l+r)
            return max(l, r) + 1
        dfs(root)
        return self.ans