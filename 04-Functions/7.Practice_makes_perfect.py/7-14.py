def f(detector):
    people=0
    for char in detector:
        if char == "+":
            people+=1
        elif char == "-":
            people -=1
        
        if people >= 3:
            return True
    return False
print(f("+-+++-+---"))
print(f("+-+-+-+-"))

