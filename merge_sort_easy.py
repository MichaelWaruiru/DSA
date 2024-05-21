def merge_sort(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        # Recursion
        merge_sort(left)
        merge_sort(right)

        # Merge
        i = 0 # Left index
        j = 0 # Right index
        k = 0 # Merged array index
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1


        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr_list = [2, 3, 5, 1, 7, 4, 4, 2, 6, 0]
merge_sort(arr_list)
print(arr_list)