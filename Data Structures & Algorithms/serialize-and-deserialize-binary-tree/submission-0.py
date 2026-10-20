# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return "x"
        serial = ""
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                serial += "x,"
            else:
                serial += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)
        print(serial)
        return serial

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        split = data.split(',')
        if split[0] == "x": return None

        root = TreeNode(split[0])
        i = 1
        q = deque([root])
        while q:
            curr = q.popleft()
            if split[i] != "x":
                curr.left = TreeNode(split[i])
                q.append(curr.left)
            i += 1
            if split[i] != "x":
                curr.right = TreeNode(split[i])
                q.append(curr.right)
            i += 1
        return root