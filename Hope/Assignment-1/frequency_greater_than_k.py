def subarr_freq_gt_k(arr, k):
    freq = {}
    l = 0
    for r in range(0, len(arr)):
        freq[arr[r]]+=1

    