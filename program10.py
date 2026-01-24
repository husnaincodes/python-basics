nums = [10, 20, 30, 20, 40, 10]
my_nums = set(nums)
nums1 = tuple(my_nums)

print(type(nums))
print(type(my_nums))
print(type(nums1))

print(len(nums1))
print(nums1[0],nums1[-1])

if 30 in nums1:
    print("Yes")
else:
    print("No")
    