def subset_sum_recursive(nums, n, h):
    if h == 0:
        return "Yes"
    if n == 0:
        return "No"

    if nums[n - 1] > h:
        return subset_sum_recursive(nums, n - 1, h)

    include = subset_sum_recursive(nums, n - 1, h - nums[n - 1])
    exclude = subset_sum_recursive(nums, n - 1, h)

    return "Yes" if include == "Yes" or exclude == "Yes" else "No"

n = int(input("Enter No. of elements in timeslot[] = "))
print(f"Enter {n} elements:")
nums = list(map(int, input().split()))
h = int(input("Enter the target sum (h): "))

print(subset_sum_recursive(nums, n, h))
