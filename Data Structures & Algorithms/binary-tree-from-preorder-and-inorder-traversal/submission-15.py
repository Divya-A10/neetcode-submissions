# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Store each value and its position in inorder
        index_map = {}

        for i, value in enumerate(inorder):
            index_map[value] = i

        # Points to the next root in preorder
        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            # No elements in this subtree
            if left > right:
                return None

            # Take the next value from preorder as the root
            root_val = preorder[preorder_index]
            preorder_index += 1

            # Create the node
            root = TreeNode(root_val)

            # Find the root's position in inorder
            root_index = index_map[root_val]

            # Build left subtree
            root.left = build(left, root_index - 1)

            # Build right subtree
            root.right = build(root_index + 1, right)

            return root

        return build(0, len(inorder) - 1)
        