def lowerbound(x, lst):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if x == lst[mid]:
            return mid
        elif x < lst[mid]:
            up = mid
        else:
            lo = mid+1
    print(lo)


value = [2, 3, 0, 11]

nums = [ 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10]




def upperbound(x,lst):
    lo, up = 0, len(lst)
    while lo < up:
        mid = (lo+up)//2
        if x == lst[mid]:
            return mid
        elif x <= lst[mid]:
            up = mid
        else:
            lo = mid+1

    print(lo)
for x in value:
    lv = lowerbound(x,nums)
    rv = upperbound(x,nums)
    print(f"  Lower bound index: {lv}, Lower bound value: {'None' if lv >= len(nums) else nums[lv]}")
    print(f"  Upper bound index: {rv}, Upper bound value: {'None' if rv >= len(nums) else nums[rv]}")