def find_two_sum(lst: list, target):
    i, j = 0, len(lst)-1
    sort_lst = sorted(lst)
    while i != j:
        found = sort_lst[i] + sort_lst[j]
        if target == found:
            return sort_lst[i], sort_lst[j]
        elif found > target:
            j -= 1
        else:
            i += 1
    return (None, )

print(*find_two_sum([1,2,6,2,7,9], 81))
def find_sum(nums, sm):
    len_nums = len(nums) -1
    for i in range(0, len_nums):
        for x in range(i + 1, len_nums):
            smm = nums[i] + nums[x]
            if nums[i] < 0 and nums[i] + nums[-1] < sm or smm > sm:
                break
            elif smm == sm:
                return str(nums[x]) + ' ' + str(nums[i])
def find_two_sum(lst: list, target):
    prev = set()
    for i in lst:
        Y = target - i
        if Y in prev:
            return i, Y
        else:
            prev.add(i)
print(find_two_sum([3,1,5,8,3,1,98,32,11], 9))
