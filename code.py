class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        val, kids = root.val, (root.left, root.right)
        if any(kids):
            return [[val] + path
                    for kid in kids
                    for path in self.pathSum(kid, sum - val)]
        return [[val]] if val == sum else []

