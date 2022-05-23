# 백준 10828: 스택

stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) > 0:
        print(stack.pop())
    else: 
        print(-1)

def size():
    print(len(stack))

def empty():
    1 if len(stack)==0 else 0

def top():
    if len(stack) > 0:
        print(stack[-1])
    else: 
        print(-1)

# if command == 'push':
# if command == 'pop':    
# if command == 'size':
# if command == 'empty':    
# if command == 'top':
push(1)
push(2)
top()
size()
empty()
pop()
pop()
pop()
size()
empty()
pop()
push(3)
empty()
top()
