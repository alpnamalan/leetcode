### AUG 14, 2025 -- P199: BINARY TREE RIGHT SIDE VIEW ###

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """ BEATS 100% IN RUNTIME """
        levels = {}
        def fill(node, lvl):
            if not node: return
            levels[lvl] = node.val # overwrite so the right-most one remains
            fill(node.left, lvl+1)
            fill(node.right, lvl+1)
        fill(root, 0)
        return [levels[l] for l in range(len(levels))]
