# leetcode-solutions

### Binary Search
Thought Process:
1. Index is found once low = high
`while low < high`
2. Right bias or left bias?
left bias: `mid = low + ((high - low) >> 1)`
right bias: `mid = low + ((high - low + 1) >> 1)`
1. Equalities are flexible, but always include/exclude mid correctly
`if (target > nums[mid])` 
then    `low = mid + 1; // mid is not target, so exclude`
else `high = mid; // mid might be target, so include`
1. If unsure, use 2 elements and observe behaviour

#### • Left bias
```py3
# Loop invariant: if found, index is between [low, high]
while low < high:
    mid = low + ((high - low) >> 1)
    if target > nums[mid]:
        low = mid + 1
    else:
        high = mid
return low if nums[low] == target else -1
```

#### • Right bias 
```py3
# Loop invariant: if found, index is between [low, high]
while low < high:
    mid = low + ((high - low + 1) >> 1)
    if target < nums[mid]:
        high = mid - 1
    else:
        low = mid
return low if nums[low] == target else -1
```

### Sort
- #### Return sorted version
```py3
sorted(toSort, reverse=True)
```
- #### Sort in-place
```py3
toSort.sort(reverse=True)
```
- #### Sort with specific key
```py3
toSort.sort(key=len)
toSort.sort(key=lambda x:(x[1], x[2]))
```
- #### Defining Custom Comparators
```py3
from functools import cmp_to_key
toSort.sort(key=cmp_to_key(lambda x, y: x - y))
```
- #### Sort Implementations
##### Quick Sort (in-place, NOT stable)
```py3
```
##### Merge Sort - Linked List (stable, NOT in-place)
```py3
```
##### Merge Sort - Arrays (stable, NOT in-place)
```py3
```

### Useful collections operations
- #### List
```py3
slice = list[includeStart:excludeEnd:skip]

list[-n:] # gets last n values with order preserved

list[:-n-1:-1] # gets last n values in reverse order
```

- #### Dict
```py3
for k in dict.keys()
for v in dict.values()
for k, v in dict.items()
```
- #### Ordered Dict
```py3
# From version 3.7 onwards: LIFO order is now guaranteed. In prior versions, popitem() would return an arbitrary key/value pair.
dict = {}
dict.popitem()

# FIFO
from collections import OrderedDict

dict = OrderedDict()
dict.popitem(last=False)
```
- #### Default Dict
```py3
from collections import defaultdict 

adj_list = defaultdict(list)   
for i in range(5): 
    adj_list[i].append(i) 
```
- #### Set
```py3
thisSet.isdisjoint(other) # whether set has no elements in common with other.

thisSet.issubset(other)
set <= other # whether every element in the set is in other.
set < other # proper subset, set <= other and set != other.

thisSet.issuperset(other) 
set >= other # whether every element in other is in the set.
set > other # proper supserset, set >= other and set != other.

union(*others)
set | other | ...
Return a new set with elements from the set and all others.

Changed in version 2.6: Accepts multiple input iterables.

intersection(*others)
set & other & ...
Return a new set with elements common to the set and all others.

Changed in version 2.6: Accepts multiple input iterables.

difference(*others)
set - other - ...
Return a new set with elements in the set that are not in the others.

Changed in version 2.6: Accepts multiple input iterables.

symmetric_difference(other)
set ^ other
Return a new set with elements in either the set or other but not both.

copy()
Return a shallow copy of the set.

add(elem)
Add element elem to the set.

remove(elem)
Remove element elem from the set. Raises KeyError if elem is not contained in the set.

discard(elem)
Remove element elem from the set if it is present.

pop()
Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

clear()
Remove all elements from the set.
```

### Common Data Structures
- #### Stack
```py3
from collections import deque

stack = deque() # initialize
stack.append(item) # push
stack.pop() # pop
if stack: # peek
    stack[-1]
```

- #### Queue
```py3
from collections import deque

stack = deque() # initialize
stack.append(item) # push
stack.popleft() # pop
if stack: # peek
    stack[0]
```

- #### Priority Queue
##### heapq
```py3
from heapq import *

# Convert list into heap
heap = [3,1,2]

heapify(heap) # convert list to minHeap
heappush(heap) # push to heap
heappop(heap) # gets smallest
heappushpop(heap, item) # push then pop
heapreplace(heap, item) # pop then push
heap[:n] # get smallest n
nlargest(k, heap) # efficient for small n
nsmallest(k, heap) # efficient for small n
```

- #### Trie
```py3
class TrieNode:
    def __init__(self):
        self.validChars = {}
        self.isEnd = False

    def contains(self, char):
        return char in self.validChars
    
    def next(self, char):
        return self.validChars.get(char, None)

    def upsert(self, char):
        if char not in self.validChars:
            self.validChars[char] = TrieNode()

    def isValid(self):
        return self.isEnd

    def end(self):
        self.isEnd = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentTrieNode = self.root
        for char in word:
            currentTrieNode.upsert(char)
            currentTrieNode = currentTrieNode.next(char)
        currentTrieNode.end()

    def search(self, word: str) -> bool:
        currentTrieNode = self.root
        for char in word:
            if not currentTrieNode.contains(char):
                return False
            currentTrieNode = currentTrieNode.next(char)
        return currentTrieNode.isValid()
        

    def startsWith(self, prefix: str) -> bool:
        currentTrieNode = self.root
        for char in prefix:
            if not currentTrieNode.contains(char):
                return False
            currentTrieNode = currentTrieNode.next(char)
        return True
```
### Common Helpers
- #### List Comprehension
```py3
# Initialize default 3D list
[[0 for _ in range(i)] for _ in range(j)]*k

# Initialize 2D list
[[1 if cell else 0 for cell in row] for row in matrix]

# Filter
[(r,c) for c in range(n) for r in range(m) if not matrix[r][c]]
```
- #### Loop/Iteration
```py3
for x, y in zip(a, b) # iterates over both simultaneously, upper bounded by shorter collection

# unpack collections using *, example: transpose matrix
zip(*matrix)
```
- #### Frequency counting
```py3
from collections import Counter
frequencyDict = Counter(toCalculate)
```
- #### Own implementation of frequency counting
```py3
def frequencyCounter(s):
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1    
    return freq
```
### Graph Traversal

#### • Inorder (Left, Root, Right) Stack [LeetCode Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
Recursive
```py3
if not root: return []
return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
```
Iterative
```py3
stack = deque()
ans = []

while root or stack:
    while root: # make sure that we traverse leftwards
        stack.append(root)
        root = root.left
    root = stack.pop()
    ans.append(root.val)
    root = root.right
        
return ans
```
General Iterative
```py3
ans, stack = [], deque([(root, False)])
while stack:
    node, visited = stack.pop()
    if node:
        if visited:
            ans.append(node.val)
        else:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))
return ans
```
#### • Preorder (Root, Left, Right) Stack [LeetCode Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
Recursive
```py3
if not root: return []
return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```
Iterative
```py3
stack = deque([root])
ans = []
while stack:
    node = stack.pop()
    if not node:
        continue
    ans.append(node.val)
    stack.append(node.right)
    stack.append(node.left)
return ans
```
General Iterative
```py3
ans, stack = [], deque([(root, False)])
while stack:
    node, visited = stack.pop()
    if node:
        if visited:
            ans.append(node.val)
        else:
            stack.append((node.right, False))
            stack.append((node.left, False))
            stack.append((node, True))
return ans
```
#### • Postorder (Left, Right, Root) Stack [LeetCode Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
Recursive
```py3
if not root: return []
return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```
Iterative
```py3
stack = deque()
while root:
    stack.append(root)
    root = root.left
processedRight = set()
ans = []
while stack:
    node = stack.pop()
    if node.right:
        if node in processedRight:
            ans.append(node.val)
        else:
            stack.append(node)
            curr = node.right
            while curr:
                stack.append(curr)
                curr = curr.left
            processedRight.add(node)
    else:
        ans.append(node.val)
return ans
```
General Iterative
```py3
ans, stack = [], deque([(root, False)])
while stack:
    node, visited = stack.pop()
    if node:
        if visited:
            ans.append(node.val)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
return ans
```
#### • Levelorder (BFS) Queue [LeetCode Levelorder Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
```py3
if not root:
    return []

traversal, currentLevel = [], [root]
while currentLevel:
    traversal.append([node.val for node in currentLevel])
    nextLevel = [(node.left, node.right) for node in currentLevel]
    currentLevel = [node for LR in nextLevel for node in LR if node]

return traversal
```

### Knapsack Problem
#### • Recursion (Memoization)
```py3
dp = {}

if (idx, amount) in dp:
    return dp[(idx, amount)]

dp[(idx, amount)] = value
```
### Graph Theory
#### Get Lowest Common Ancestor [LeetCode LCA of BST Problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
```py3
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root in [p, q, None]:
        return root

    left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
    
    return root if left and right else left or right
```
#### Topological Sort [LeetCode Course Schedule 2 Problem](https://leetcode.com/problems/course-schedule-ii/)
- Time: O(V + E), Space: O(E)
```py3
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    outEdges = [[a for (a, b) in prerequisites if b == i] for i in range(numCourses)]
    inOrder = [len([1 for (a, b) in prerequisites if a == i]) for i in range(numCourses)]

    ans = []
    frontier = deque(edge for edge, order in enumerate(inOrder) if order <= 0)
    while frontier:
        currVertice = frontier.popleft()
        ans.append(currVertice)
        for edge in outEdges[currVertice]:
            inOrder[edge] -= 1
            if inOrder[edge] <= 0:
                frontier.append(edge)

    return ans if len(ans) == numCourses else []
```
#### Dijkstra's Algorithm [LeetCode Minimum Cost Problem](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- Does not work if there is a negative weighted cycle
- Time: O((V+E)lgV) = O(ElgV), Space: O(V)
```py3
adj_list = defaultdict(list)
for frm, to, price in flights:
    adj_list[frm].append((to,price))

explored = {}
frontier = [(0, -1, src)]
# when exploring, I am reaching the current node with least cost with maximum k steps
while frontier:
    cost, stop, city = heappop(frontier)
    if stop > k or city in explored and stop >= explored[city]: 
        # if explored, we only explore if step is lower
        continue
    if city == dst:
        return cost
    explored[city] = stop
    for to, price in adj_list[city]:
        heappush(frontier, (cost+price, stop+1, to))
return -1
```

#### Bellman Ford Algorithm [LeetCode Minimum Cost Problem](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- Detects & Works with negative weighted cycle
- Time: O(EV), Space: O(V)
```py3
minPrice = [math.inf]*n
minPrice[src] = 0

for _ in range(k+1):
    relaxed = [*minPrice] # unpack and put in list, essentially a copy
    for frm, to, price in flights:
        if minPrice[frm] + price < relaxed[to]:
            relaxed[to] = minPrice[frm] + price
    minPrice = relaxed

return -1 if minPrice[dst] == math.inf else minPrice[dst]
```

#### Minimum Spanning Tree [LeetCode MST Problem](https://leetcode.com/problems/min-cost-to-connect-all-points/)
> prim's algorithm
- Good for dense graphs
- Time: O(ElgV), Space: O(V)
```py3
def calcDist(point1, point2):
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

included, minHeap = set(), [(0, 0)]
minimumCost, numPoints = 0, len(points)
while len(included) < numPoints:
    dist, to = heappop(minHeap)
    if to in included:
        continue
    minimumCost += dist
    included.add(to)
    # include edges from newly added vertice
    sourcePoint = points[to]
    for destPointIdx, destPoint in enumerate(points):
        if destPointIdx not in included:
            heappush(minHeap, (calcDist(sourcePoint, destPoint), destPointIdx))
return minimumCost
```
