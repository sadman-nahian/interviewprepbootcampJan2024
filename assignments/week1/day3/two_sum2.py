def twoSum(numbers,target):
    l,r=0,len(numbers)-1
    while(l<r):
        if numbers[l]+numbers[r]>target:
            r-=1
            continue
        if numbers[l]+numbers[r]<target:
            l+=1
            continue
        if numbers[l]+numbers[r]==target:
            return [l+1,r+1]
    return None
numbers = [2,7,11,15]
print(twoSum(numbers,9))


        