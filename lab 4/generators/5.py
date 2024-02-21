def down(a):
    while a >= 0:
        yield a
        a -= 1
a = int(input())
nums = []
for x in down(a):
    nums.append(x)
print(nums)