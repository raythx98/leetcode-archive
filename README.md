# leetcode-solutions

### Binary Search

#### • Minimum position with duplicates
```
int low = 0;
int high = size - 1;

// Loop invariant: index is between [low, high+1]

while (low <= high) {
    int mid = low + ((high-low)>>1);
    if (val[mid] < target) {
        low = mid + 1;
    } else {
        high = mid - 1;
    }
}
```

#### • Maximum position with duplicates
```
int low = 0;
int high = size - 1;

// Loop invariant: index is between [low-1, high]

while (low <= high) { 
    int mid = low + ((high-low)>>1);
    if (val[mid] <= target) {
        low = mid + 1;
    } else {
        high = mid - 1;
    }
}
```

### Sort

#### • Quick Sort (in-place, NOT stable)
```
int partition(vector<int> &values, int left, int right) {
    int mid = left + (right - left) / 2;
    int val = values[mid];
    while(left <= right) {
        while(values[left] < val) {
            left++;
        }
        while(values[right] > val) {
            right--;
        }
        if(left <= right) {
            int temp = values[left];
            values[left] = values[right];
            values[right] = temp;
            left++;
            right--;
        }
    }
    return left;
}

void quicksort(vector<int> &values, int left, int right) {
    if(left < right) {
        int pivotIndex = partition(values, left, right);
        quicksort(values, left, pivotIndex - 1);
        quicksort(values, pivotIndex, right);
    }
}
```
#### • Merge Sort - Linked List (stable, NOT in-place)
```
```
#### • Merge Sort - Arrays (stable, NOT in-place)
```
void outPlaceMerge(vector<int> &nums, int low, int mid, int high) {
    if (low >= high) return;
    int l = low;
    int r = mid + 1;
    int k = 0;
    int size = high - low + 1;
    vector<int> sorted(size, 0);
    while (l <= mid and r <= high)
        sorted[k++] = nums[l] < nums[r] ? nums[l++] : nums[r++];
    while (l <= mid) 
        sorted[k++] = nums[l++];
    while (r <= high) 
        sorted[k++] = nums[r++];
    for (k = 0; k < size; k++)
        nums[k + low] = sorted[k];
}

void mergeSort(vector<int> &nums, int low, int high) {
    if (low >= high) return;
    int mid = (high - low) / 2 + low;
    mergeSort(nums, low, mid);
    mergeSort(nums, mid + 1, high);
    outPlaceMerge(nums, low, mid, high);
}
```
#### • Radix Sort (stable, in-place, `O(d(n+k))`)
```
```
### Graph Traversal

#### • BFS (Queue)
```
```
#### • BFS (Recursion)
```
```
#### • DFS (Stack)
```
```
#### • DFS (Recursion)
```
```
### Knapsack Problem
#### • Recursion (Memoization)
```
map<int, map<int, int>> dp;
    
int dp_contains(int target, int index) {
    if (dp.count(target)) {
        if (dp[target].count(index)) return true;
        return false;
    }
    return false;
}

int read(int target, int index) {
    return dp[target][index];
}

void write(int target, int index, int val) {
    dp[target][index] = val;
}
```
#### • DP Table (2D) - [LeetCode Coin Change 1 Problem](https://leetcode.com/problems/coin-change/)
```
int coinChange(vector<int>& coins, int amount) {
    if (amount == 0) return 0;
    int dp[coins.size()][amount+1];
    for (int row = 0; row < coins.size(); row++) {
        dp[row][0] = 0;
        for (int col = 1; col < amount + 1; col++) {
            dp[row][col] = INT_MAX;
            int test_col = col-coins[row];
            int row_min = test_col >= 0 && dp[row][test_col] != INT_MAX 
                    ? dp[row][test_col] + 1
                    : INT_MAX;
            int prev_min = row > 0 ? dp[row-1][col] : INT_MAX;
            dp[row][col] = min(prev_min, row_min);

        }
    }
    return dp[coins.size()-1][amount] > amount ? -1 : dp[coins.size()-1][amount];
}
```
#### • DP Table (Rolling 1D) [LeetCode Coin Change 2 Problem](https://leetcode.com/problems/coin-change-2/)
```
int change(int amount, vector<int>& coins) {
    if (amount == 0) return 1;
    if (coins.empty()) return 0;
    int dp[amount+1];
    dp[0] = 1;
    for (int i = 1; i < amount + 1; i++) {
        dp[i] = 0;
    }
    for (auto &c: coins) {
        for (int i = 1; i < amount + 1; i++) {
            dp[i] = i - c >= 0 ? dp[i - c] + dp[i] : dp[i];
        }
    }
    return dp[amount];
}
```
