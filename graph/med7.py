### AUG 15, 2025 -- P230: K-TH SMALLEST ELEMENT IN A BST ###

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """ BEATS 100% IN RUNTIME """
        arr = []
        def process(node, out):
            if node:
                process(node.left, out)
                out.append(node.val)
                process(node.right, out)
        process(root, arr)
        return arr[k-1]
