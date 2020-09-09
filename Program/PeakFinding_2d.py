from math import ceil

arr = [[10, 20, 15, 12],
       [21, 16, 14, 13],
       [ 7, 16, 14, 20]]

def findMax(arr, rows, mid, max):
    """
    Find maximum element in the mid_column, return max_value and row_index
    """
    max_index = 0
    for i in range(rows):
        if (max < arr[i][mid]):
            max = arr[i][mid]
            max_index = i
    return max, max_index

def findPeakUtil(arr, rows, columns, mid):
    # Evaluating maximum of mid column.
    # Note max is passed by reference.
    max = 0
    max, max_index = findMax(arr, rows, mid, max)

    # peak on the first or last column
    if (mid == 0 or mid == columns - 1):
        return max

    # If mid column maximum is also peak
    if (max >= arr[max_index][mid - 1] and max >= arr[max_index][mid + 1]):
        return max

    # If max is less than its left
    if (max < arr[max_index][mid - 1]):
        return findPeakUtil(arr, rows, columns, mid - ceil(mid / 2.0))

    # If max is less than its right
    return findPeakUtil(arr, rows, columns, mid + ceil(mid / 2.0))

def findPeak(arr, rows, columns):
    return findPeakUtil(arr, rows, columns, columns // 2)

rows = len(arr)
columns = len(arr[0])
print(findPeak(arr, rows, columns))