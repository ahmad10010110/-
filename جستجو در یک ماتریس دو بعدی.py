def binary_search_matrix(matrix, target):

  m, n = len(matrix), len(matrix[0])
  low, high = 0, m - 1

  while low <= high:
    mid = (low + high) // 2
    if matrix[mid][0] > target:
      high = mid - 1
    elif matrix[mid][-1] < target:
      array = matrix[mid]
      if binary_search_array(array, target):
          return True
      low = mid + 1
    else:
      i = low
      while i <= high:
        j = (i + high) // 2
        if matrix[mid][j] > target:
          high = j - 1
        elif matrix[mid][j] < target:
          i = j + 1
        else:
          return True
      return False

  return False



matrix = [
    [1,3,5],
    [7,8,10],
    [12,15,18]
    ]
target = 8

print(binary_search_matrix(matrix, target))

