def count_subsets_with_sum(arr, target_sum):
    n = len(arr)
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(n + 1)]
    
   
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(0, target_sum + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
    
    return dp[n][target_sum]
arr = list(map(int, input().split()))
target_sum = int(input())

result = count_subsets_with_sum(arr, target_sum)

print(f"Total number of subsets with the given sum is: {result}")