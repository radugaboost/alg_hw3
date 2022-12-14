#Сложность данного алгоритма O(n)
#Проходимся по всему дереву и сохраняем связи между ячейками

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        result = []
        if root.left: 
            for path in self.binaryTreePaths(root.left):
                result.append(str(root.val) + "->" + path)
        if root.right: 
            for path in self.binaryTreePaths(root.right):
                result.append(str(root.val) + "->" + path)
        return result
