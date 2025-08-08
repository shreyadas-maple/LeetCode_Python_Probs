def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Save the indices that add up to target
    pos = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                pass
            else:
                if nums[i] + nums[j] == target:
                    if i not in pos:
                        pos.append(i)
                    if j not in pos:
                        pos.append(j)
    return pos

print(twoSum(nums = [2,7,11,15], target=9))
