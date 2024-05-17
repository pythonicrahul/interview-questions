class Stack:

    stack = []

    def __init__(self):
        print("Stack initalized")
    
    def __str__(self):
        output  = []
        for i, item in enumerate(self.stack):
            output.append(f"{i} -> {item}")
        return str(output)

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        if len(self.stack):
            return self.stack[0]
        return -1
        

if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    stack1.push(5)

    print(stack1)

    print(stack1.pop())

    print(stack1)