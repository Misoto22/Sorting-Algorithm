def selection_sort(list:list) -> list:
    for i in range(0, len(list)-1):
        minValue = list[i]
        minIndex = i
        for j in range(i+1, len(list)):
            if list[j] < minValue:
                minValue = list[j]
                minIndex = j
        if minIndex != i:
            list[minIndex] = list[i]
            list[i] = minValue
    return list


# Time Complexity: O(n^2)

# Test Case 1
# Expected Output: [1, 2, 3, 4, 5]
print(selection_sort([5, 4, 3, 2, 1]))

# Test Case 2
# Expected Output: [1, 2, 3, 4, 5]
print(selection_sort([1, 2, 3, 4, 5]))

# Test Case 3  
# Expected Output: [1, 2, 3, 4, 5]
print(selection_sort([3, 2, 1, 5, 4]))