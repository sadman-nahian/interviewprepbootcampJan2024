def threeSum(nums):
    if len(nums) < 3:
        return []

    result = set()
    nums.sort()

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break  # No need to continue if the first element is positive
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates

        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return list(result)

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
