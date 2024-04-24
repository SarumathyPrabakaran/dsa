
def get_num_subarrays(arr,k):
    l = 0
    now = 0
    ans = 0
    for r in range(0,len(arr)):
        now+=arr[r]


        while now>=k:
            if now==k:
                ans+=1
            now-=arr[l]
            l+=1
        
    return ans



l = [5,1,3,1,1,5,5]
k = 5
ans = get_num_subarrays(l,k)
print(ans)