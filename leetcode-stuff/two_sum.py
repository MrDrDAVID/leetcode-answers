nums1 = [1, 3, 7, 8, 10, 14]
target1 = 10

def twoSum(nums, target):
    """
    functions that takes in a list of integers and a target value
    and returns the indices of two elements whos sum is equal to target value
    """
    for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]

numbers = twoSum(nums1 ,target1)

print(f'The indices that equal the target value are: ', end='')
print(numbers)
print(f'And the values that equal the target value {target1} are: {nums1[1]} and {nums1[2]}')