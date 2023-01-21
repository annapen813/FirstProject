A = [41, 33, 25, 10, 39, 23, 31, 32, 1, 21, 28, 13, 5]

# Traverse through all array elements
for i in range(0, len(A)):
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

print(A)
