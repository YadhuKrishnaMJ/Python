def subsets(nums):
    currset, subset = [],[]
    backtrack(0,nums,currset,subset)
    return len(subset)
def backtrack(i,nums,currset,subset):
    if i == len(nums) and sum(currset) == 1:
        subset.append(currset.copy())
        return
    if i == len(nums):
        return
    
    #include 
    currset.append(nums[i])
    backtrack(i+1,nums,currset,subset)
    currset.pop()

    #dont include
    backtrack(i+1,nums,currset,subset)

print(subsets([0,1,0]))