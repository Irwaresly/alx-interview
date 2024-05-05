def canUnlockAll(boxes):
    # Create a set to keep track of the boxes that have been visited
    visited = set()
    
    # Add the first box to the visited set
    visited.add(0)
    
    # Create a stack to store the keys
    stack = [0]
    
    # Iterate through the stack until it is empty
    while stack:
        # Pop the top box from the stack
        box = stack.pop()
        
        # Iterate through the keys in the current box
        for key in boxes[box]:
            # If the key opens a new box and it hasn't been visited yet, add it to the stack and visited set
            if key < len(boxes) and key not in visited:
                stack.append(key)
                visited.add(key)
    
    # If all boxes have been visited, return True. Otherwise, return False.
    return len(visited) == len(boxes)
