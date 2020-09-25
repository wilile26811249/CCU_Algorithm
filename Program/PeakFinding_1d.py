arr = [3, 2, 1, 4, 7, 6, 3, 2, 1]
length = len(arr)
ans = []

def find_peak_iteration(arr):
    """
    Solution: For loop, iteration
    Time Complexity is O(n)
    """
    global ans
    for i in range(1, length - 1):
        if i == 1:
            if arr[0] >= arr[i]:
                ans.append(i)
        elif i == length:
            if arr[i] >= arr[i - 1]:
                ans.append(i)
        else:
            if arr[i - 1] <= arr[i] and arr[i] >= arr[i + 1]:
                ans.append(i)
    return ans

def findPeakUtil(arr, left, right, n):
    """
    Solution: Divide and conquer
    Time Complexity is O(logN) base 2
    """
    mid = (left + right) // 2
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] >= arr[mid]):
        return mid
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return findPeakUtil(arr, left, (mid - 1), n)
    else:
        return findPeakUtil(arr, mid + 1, right, n)

def findPeak(arr, n):
    return findPeakUtil(arr, 0, n - 1, n)

print(find_peak_iteration(arr))
print(findPeak(arr, length))
