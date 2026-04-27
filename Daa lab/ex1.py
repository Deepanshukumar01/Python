def quick_sort(arr):
    if len(arr) <= 1:
        return arr
   
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
   
    return quick_sort(left) + middle + quick_sort(right)


data = [10, 71, 8, 9, 17, 50]
sorted_data = quick_sort(data)
print("Sorted array:", sorted_data)