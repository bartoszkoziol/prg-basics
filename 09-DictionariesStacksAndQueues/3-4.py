import queue

def decimal_to_binary(number):
    if number<0:
        return "Invalid input: Number must be non-negative"
    
    stack=queue.LifoQueue()

    if number==0:
        return 0
    
    while number>0:
        remainder=number%2
        stack.put(remainder)
        number=number//2

    binary_number = ""
    while not stack.empty():
        binary_number+=str(stack.get())

    return binary_number

print(decimal_to_binary(18))
print(decimal_to_binary(-5))   # "Invalid input: Number must be non-negative"
print(decimal_to_binary(0))