# Binary search also known as Bisection Search
numbers = [42, 419, 215, 71, 58, 48, 172, 134, 158, 372, 256, 129, 8, 24, 162, 375, 428, 453, 309, 231, 275, 372, 247, 154, 272, 246, 1, 488, 463, 8, 124, 487, 176, 172, 470, 189, 215, 302, 103, 27, 396, 321, 22, 49, 495, 481, 169, 53, 336, 87, 430, 362, 500, 43, 170, 444, 232, 228, 281, 110, 112, 490, 306, 80, 215, 25, 396, 244, 439, 322, 294, 4, 374, 211, 219, 308, 219, 354, 156, 81, 239, 94, 43, 274, 266, 127, 382, 166, 73, 119, 53, 146, 307, 78, 73, 430, 110, 18, 204, 311]

numbers.sort() # TimSort 0 (n log n)

def binary_search(numbers_list, number, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if number == numbers_list[mid]:
        return mid
    elif number < numbers_list[mid]:
        return binary_search(numbers_list, number, left, mid-1)
    else:
        return binary_search(numbers_list, number, mid+1, right)
    
# print(numbers)
print(binary_search(numbers, 231, 0, len(numbers) - 1))