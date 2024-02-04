def spy_game(nums):
    found_0 = False
    found_0_0 = False
    found_0_0_7 = False 

    for num in nums:
        if num == 0:
            found_0 = True
        elif num == 0 and found_0:
            found_0_0 = True
        elif num == 7 and found_0_0:
            found_0_0_7 = True

    return found_0_0_7

# Test cases
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([0, 1, 7, 2, 0, 4, 5, 0]))  # False
