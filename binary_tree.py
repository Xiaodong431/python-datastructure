
def build_binary_tree(nums, start):
	if start >= len(nums): return None
	if nums[start] == '#': return None
	root = TreeNode(nums[start])
	root.left = build_binary_tree(nums,2*start+1)
	root.right = build_binary_tree(nums,2*start+2)
	return root

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def postorder(self):
		stack = [self]
		ans = []
		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
		return ans[::-1]

	def inorder(self):
		def go_left_bottom(stack, node):
			stack.append(node)
			while node.left:
				node = node.left
				stack.append(node)
			return node
		ans = []
		stack = []
		go_left_bottom(stack,self)
		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.right:
				go_left_bottom(stack,node.right)
			while stack and node == stack[-1].right:
				node = stack.pop()
		return ans

	def preorder(self):
		stack = [self]
		ans = []
		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		return ans

tree = build_binary_tree([1,2,3,4,5,6,7,8,9,10], 0)
print(tree.postorder())
print(tree.inorder())
print(tree.preorder())


tree = build_binary_tree([1,2,3,4,'#',6,'#',8,9,'#','#',12,'#'], 0)
print(tree.postorder())
print(tree.inorder())
print(tree.preorder())
def build_binary_tree(nums, start):
	if start >= len(nums): return None
	if nums[start] == '#': return None
	root = TreeNode(nums[start])
	root.left = build_binary_tree(nums,2*start+1)
	root.right = build_binary_tree(nums,2*start+2)
	return root

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def postorder(self):
		stack = [self]
		ans = []
		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.left:
				stack.append(node.left)
			if node.right:
				stack.append(node.right)
		return ans[::-1]

	def inorder(self):
		def go_left_bottom(stack, node):
			stack.append(node)
			while node.left:
				node = node.left
				stack.append(node)
			return node
		ans = []
		stack = []
		go_left_bottom(stack,self)
		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.right:
				go_left_bottom(stack,node.right)
			while stack and node == stack[-1].right:
				node = stack.pop()
		return ans

	def preorder(self):
		stack = [self]
		ans = []
		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		return ans
"""
tree = build_binary_tree([1,2,3,4,5,6,7,8,9,10], 0)
print(tree.postorder())
print(tree.inorder())
print(tree.preorder())


tree = build_binary_tree([1,2,3,4,'#',6,'#',8,9,'#','#',12,'#'], 0)
print(tree.postorder())
print(tree.inorder())
print(tree.preorder())
"""
