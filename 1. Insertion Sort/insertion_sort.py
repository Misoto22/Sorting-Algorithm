def insertion_sort(list: list) -> list:
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j] #Swap
            else:
                break
    return list

# Time Complexity: O(n^2)

# Test Case 1
# Expected Output: [1, 2, 3, 4, 5]
print(insertion_sort([5, 4, 3, 2, 1]))

# Test Case 2
# Expected Output: [1, 2, 3, 4, 5]
print(insertion_sort([1, 2, 3, 4, 5]))

# Test Case 3  
# Expected Output: [1, 2, 3, 4, 5]
print(insertion_sort([3, 2, 1, 5, 4]))