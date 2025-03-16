#line1
#Given an array of integers nums and an integer target, return the indices of the two numbers that add up to the target.

def two_sum(nums, target):
    num_map = {}  
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]  
        num_map[num] = i  
    return []  


nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))


result = two_sum(nums, target)
if result:
    print(f"Indices of numbers that add up to {target}: {result}")
else:
    print("No two numbers add up to the target.")
