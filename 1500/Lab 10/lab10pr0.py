"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 10 Part 0
04/26/2018"""

class TreeNode:
    
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def getheight(root):
    """ Find the height of a binary search tree
        Args:
            root (Node): the root of the tree
        Returns:
            value (int): height of the tree
    """

    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 0
    else:
        return 1 + max(getheight(root.left), getheight(root.right))
f = TreeNode(10)
f.left = TreeNode(8)
f.right = TreeNode(12)
f.left.left = TreeNode(4)

print(getheight(f))

