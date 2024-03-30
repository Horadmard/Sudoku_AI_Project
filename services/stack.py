class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# test:
# my_stack = Stack(10, "hello")
# print("Parameters:", my_stack.value, my_stack.lo)

# my_stack.push(5)
# my_stack.push(8)
# my_stack.push(3)

# print("Stack size:", my_stack.size())
# print("Top element:", my_stack.peek())

# popped_item = my_stack.pop()
# print("Popped item:", popped_item)