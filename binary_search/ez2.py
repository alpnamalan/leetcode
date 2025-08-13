### AUG 13, 2025 -- P108: CONVERT SORTED ARRAY TO BINARY SEARCH TREE ###

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo, hi):
            if lo >= hi: return None
            mid = (lo+hi)//2
            newNode = TreeNode(nums[mid])
            newNode.left = build(lo, mid)
            newNode.right = build(mid+1, hi)
            return newNode
        return build(0, len(nums))
