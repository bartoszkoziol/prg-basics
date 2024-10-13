#A tree may be cut down if its diameter is at least 50 cm. Write a program that, 
# based on the circumference of the tree entered from the keyboard, calculates# and displays the value True 
# if the tree can be cut down, or display the value False otherwise.

circumference = float(input("Enter tree circumference(cm): "))
tree_to_cut = circumference >= 120
print(f"Tree can be cut: {tree_to_cut}")
