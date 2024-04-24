

def get_max_consec_ones(arr):
    n = len(arr)
    l, r = 0, 0
    ans = 0
    while(r<n):
        if arr[l]==0:
            l+=1
            r = l
        elif arr[r]==0:
            ans = max(ans, r-l)
            l = r
        r+=1

    if arr[-1]:
            ans = max(ans,r-l+1)
    return ans


def findMaxConsecutiveOnes(self, nums) -> int:
        count = 0
        max_consecutives = 0
        for num in nums:
            if num == 1:
                count+=1
            else:
                max_consecutives = max(max_consecutives, count)
                count = 0
        max_consecutives = max(max_consecutives, count)
        return max_consecutives
    


l = [1,1,0,1,1,1]
ans = get_max_consec_ones(l)
print(ans)


        

