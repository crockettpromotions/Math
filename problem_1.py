nums = []
for i in range(0, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        nums.append(i)

sum_nums = sum(nums)
print(nums)
print(sum_nums)

print(10 % 3)