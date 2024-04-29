nums = list(map(int, input().split()))
nums.sort()
for i in range(0, len(nums)):
    print(nums[i], end=" " if i != len(nums) - 1 else "\n")
