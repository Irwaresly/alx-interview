def canUnlockAll(boxes):
    if not boxes:
        return False
    
    visited = set()
    queue = [0]  # Start from the first box
    visited.add(0)
    
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                queue.append(key)
                visited.add(key)
    
    return len(visited) == len(boxes)

# Example usage
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True
    
    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True
    
    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False

