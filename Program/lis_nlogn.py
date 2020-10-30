def ceil_index(arr, left, right, key):
    while right - left > 1:
        m = (left + right) // 2
        if arr[m] >= key:
            right = m
        else:
            left = m
    return right

def LongestIncreasingSubsequenceLength(arr, size):
    tail_arr = [0 for i in range(size + 1)]
    tail_arr[0] = arr[0]

    length = 1
    for i in range(1, size):
        if arr[i] < tail_arr[0]:
            tail_arr[0] = arr[i]
        elif arr[i] > tail_arr[length - 1]:
            tail_arr[length] = arr[i]
            length += 1
        else:
            tail_arr[ceil_index(tail_arr, -1, length - 1, arr[i])] = arr[i]
    return length

lst = [ 2, 5, 3, 7, 11, 8, 10, 13, 6, 14]
n = len(lst)

print("Length of Longest Increasing Subsequence is ",
      LongestIncreasingSubsequenceLength(lst, n))