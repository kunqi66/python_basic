import sys
def fun(arr):
    if len(arr) == 1:
        return 0
    nums = [10**1000 for i in range(len(arr))]
    nums[0] = 0
    nums[1]=1
    for i in range(2,len(nums)):
        lun = nums[i]
        j = 0
        while j < i:
            if arr[i] == arr[j]:
                lun=min(nums[j]+1,lun)
            if lun + 1 < nums[i-1]:
                nums[i-1] = lun+1
                j-=1
            else:
                j+=1
        nums[i] = lun
    return nums[len(nums)-1]


arr = [100,-23,-23,404,100,23,23,23,3,404]
print(fun(arr))
