class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None


root = Node(value='CEO')
root.left = Node('CTO')
root.right = Node('CFO')
root.left.left = Node('Devmgr')

root.left.right = Node('QA')

root.right.right = Node('Finance')

#node-left-right
def pre_order(node):
  if node:
    print(node.value)
    pre_order(node.left)
    pre_order(node.right)

#left-node-right
def in_order(node):
  if node:#base-case
    in_order(node.left)
    print(node.value)
    in_order(node.right)

#left-right-node
def post_order(node):
  if node:
    post_order(node.left)
    post_order(node.right)
    print(node.value)


from collections import deque

def level_order(root):
  if not root:
    return 
  queue = deque([root])
  while queue:
    current = queue.popleft()
    print(current.value)
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right) 

bst_root = Node(8)
bst_root.left = Node(3)
bst_root.right = Node(10)
bst_root.left.left = Node(1)
bst_root.left.right = Node(6)
bst_root.right.left = Node(14)
bst_root.right.right = Node(13)



if __name__ == "__main__":
	print("Pre-order Traversal:")
	pre_order(root)

	print("\nIn-order Traversal:")
	in_order(root)

	print("\nPost-order Traversal:")
	post_order(root)

	print("\nLevel-order Traversal:")
	level_order(root)
   

	print("\nPre-order Traversal (BST):")
	pre_order(bst_root)

	print("\nIn-order Traversal (BST):")
	in_order(bst_root)

	print("\nPost-order Traversal (BST):")
	post_order(bst_root)

	print("\nLevel-order Traversal (BST):")
	level_order(bst_root)