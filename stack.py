class Stack:
  def __init__(self):
    self.items = []

  def push(self,item):
    self.items.append(item)
    print(f"pushed {item} to stack:{self.items}")

  def pop(self):
    if not self.isEmpty():

      removed = self.items.pop()
      print(f"Popped {removed}from stack:{self.items}")
      return removed
    else:
      print('Stack is empty.Nothing to pop')
      return None

  def peek(self):
    if not self.isEmpty():
      print(f"the top of stack is:{self.items[-1]}")
      return self.items[-1]
    else:
      print("stack is empty No top element")
      return None  
  def isEmpty(self):
    return len(self.items)  == 0
    
if __name__ == "__main__":
	stack = Stack()
	stack.push("Task 1")
	stack.push("Task 2")
	stack.push("Task 3")

	stack.peek()

	stack.pop()
	stack.pop()
	stack.pop()
	stack.pop()    
         