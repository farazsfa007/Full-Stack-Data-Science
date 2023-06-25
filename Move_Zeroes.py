def move_Zeroes(nums):
    # Initialize pointers i and j
    i = j = 0  

    # Iterate through the array
    while i < len(nums):
        if nums[i] != 0:
            # Swap non-zero element with element at position j
            nums[i], nums[j] = nums[j], nums[i]
            # Increment j
            j += 1  
             # Increment i
        i += 1 

# Example usage
nums = [0, 1, 0, 3, 12]
move_Zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]