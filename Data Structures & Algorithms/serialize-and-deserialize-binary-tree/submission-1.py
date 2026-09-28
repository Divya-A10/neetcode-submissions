# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if node is None:
                result.append("null")
                return

            result.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(result)

    def deserialize(self, data):
        data = data.split(",")
        index = 0

        def build():
            nonlocal index

            value = data[index]

            if value == "null":
                index += 1
                return None

            node = TreeNode(int(value))
            index += 1

            node.left = build()
            node.right = build()

            return node

        return build()
