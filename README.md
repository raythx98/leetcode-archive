# leetcode-solutions

### Defining Custom Comparators
```
class Compare {
public:
    bool operator() (pair<int, string> &pair1, pair<int, string> &pair2){
        if (pair1.first == pair2.first) return pair1.second > pair2.second;
        
        return pair1.first < pair2.first;
    }
};
```

#### • Declaring a Priority Queue

```
priority_queue<pair<int, string>, vector<pair<int, string>>, Compare> pq;

pq.push({i.second, i.first});
pq.top().second);
pq.pop();
```

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
void TopDownMerge(vector<int> &nums, int low, int mid, int high) {
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
    TopDownMerge(nums, low, mid, high);
}
```
#### • Radix Sort (stable, in-place, _O(d(n+k))_)
```
    int getNthDigit(int num, int n) {
        return num/pow(10, n)%10;
    }
    
    void countSort(vector<int>& nums, int digit) {
        int count[10] = {0};
        for (auto &i : nums) {
            count[getNthDigit(i, digit)]++;
        }
        for (int i = 1; i < 10; i++) {
            count[i] += count[i-1];
        }
        for (int i = 9; i > 0; i--) {
            count[i] = count[i-1];
        }
        count[0] = 0;
        vector<int> new_nums(nums.size(), 0);
        for (auto &i : nums) {
            new_nums[count[getNthDigit(i, digit)]++] = i;
        }
        nums = new_nums;
    }
    
    vector<int> sortArray(vector<int>& nums) {
        vector<int> positives;
        vector<int> negatives;
        for (auto &num : nums) {
            if (num >= 0) {
                positives.push_back(num);
            } else {
                negatives.push_back(-num);
            }
        }
        for (int i = 0; i < 6; i++) {
            countSort(positives, i);
            countSort(negatives, i);
        }
        for (auto &num : negatives) {
            num = -num;
        }
        reverse(negatives.begin(), negatives.end());
        negatives.insert(negatives.end(), positives.begin(), positives.end());
        return negatives;
    }
```
### Graph Traversal

#### • Inorder (Left, Root, Right) Stack
```
void addLeft(stack<TreeNode*> *node_stack, TreeNode* node) {
    while(node) {
        node_stack->push(node);
        node = node->left;
    }
}

vector<int> inorderTraversal(TreeNode* root) {
    if (!root) return {};
    stack<TreeNode*> node_stack;
    addLeft(&node_stack, root);
    vector<int> ans;
    while(!node_stack.empty()) {
        TreeNode* curr = node_stack.top();
        node_stack.pop();
        ans.push_back(curr->val);
        if (curr->right) addLeft(&node_stack, curr->right);
    }
    return ans;
}
```
#### • Preorder (Root, Left, Right) Stack
```
vector<int> preorderTraversal(TreeNode* root) {
    if (!root) return {};
    stack<TreeNode*> node_stack;
    vector<int> ans;
    node_stack.push(root);
    while (!node_stack.empty()) {
        TreeNode* curr = node_stack.top();
        node_stack.pop();
        ans.push_back(curr->val);
        if (curr->right) node_stack.push(curr->right);
        if (curr->left) node_stack.push(curr->left);
    }
    return ans;
}
```
#### • Postorder (Left, Right, Root) Stack
```
if (!root) return {};
vector<TreeNode*> explored_rhs;
stack<TreeNode*> node_stack;
addLeft(&node_stack, root);
vector<int> ans;
while(!node_stack.empty()) {
    TreeNode* curr = node_stack.top();
    if (curr->right && find(explored_rhs.begin(), explored_rhs.end(), 
                            curr->right) == explored_rhs.end()) {
        explored_rhs.push_back(curr->right);
        addLeft(&node_stack, curr->right);
        continue;
    }
    node_stack.pop();
    ans.push_back(curr->val);
}
return ans;
}
```
#### • Levelorder (BFS) Queue
```
vector<int> levelOrder(TreeNode* root) {
    if (!root) return {};
    queue<TreeNode*> node_queue;
    vector<int> ans;
    node_queue.push(root);
    while (!node_queue.empty()) {
        TreeNode* curr = node_queue.front();
        node_queue.pop();
        if (curr->left) node_queue.push(curr->left);
        if (curr->right) node_queue.push(curr->right);
        ans.push_back(curr->val);
    }
    return ans;
}
```
#### • DFS (Recursion)
```
vector<int> ans;
if (!root) return;
ans.push_back(root->val);
if (root->left) recurse(root->left);
if (root->right) recurse(root->right);
return ans;
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
### Graph Theory
#### Topological Sort [LeetCode Course Schedule 2 Problem](https://leetcode.com/problems/course-schedule-ii/)
```
// build graph
vector<vector<int>> out_edges(numCourses, vector<int>());
vector<int> in_degree(numCourses, 0);
queue<int> frontier; // frontier always has in-degree == 0
vector<int> ans;


for (auto &prerequisite: prerequisites) {
    in_degree[prerequisite.front()]++;
    out_edges[prerequisite.back()].push_back(prerequisite.front());
};

for (int i = 0; i < numCourses; i++) {
    if (!in_degree[i]) {
        frontier.push(i);
    }
}

while (!frontier.empty()) {
    int pop_node = frontier.front();
    frontier.pop();
    ans.push_back(pop_node);
    for (auto &edge: out_edges[pop_node]) {
        if (!--in_degree[edge]) {
            frontier.push(edge);
        }
    }
}

return ans.size() == numCourses ? ans : vector<int>();
```
