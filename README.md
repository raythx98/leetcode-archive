# leetcode-solutions

### Sort
- #### Return sorted version
```py3
sorted(toSort, reverse=True)
```
- #### Sort in-place
```py3
toSort.sort(reverse=True)
```
- #### Defining Custom Comparators
```py3
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
```

- #### Dict
```py3
for k in dict.keys()
for v in dict.values()
for k, v in dict.items()
```
- #### Ordered Dict
```py3

```
- #### Set
```py3
thisSet.isdisjoint(other) # whether set has no elements in common with other. Diisjoint is empty set

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

heapify(heap)
heappush(heap)
heappop(heap) # gets smallest
heappushpop(heap, item) # push then pop
heapreplace(heap, item) # pop then push
nlargest(k, heap)
nsmallest(k, heap)
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

# Convert list into heap
heap = [3,1,2]

heapify(heap)
heappush(heap)
heappop(heap) # gets smallest
heappushpop(heap, item) # push then pop
heapreplace(heap, item) # pop then push
nlargest(k, heap)
nsmallest(k, heap)
```

### Common Helpers
- #### List Comprehension
```py3
# Initialize 2D list
[[1 if cell else 0 for cell in row] for row in matrix]

# Filter
[(r,c) for c in range(n) for r in range(m) if not matrix[r][c]]
```
- #### Loop/Iteration
```py3
for x, y in zip(a, b) # iterates over both simultaneously, upper bounded by shorter collection
```
- #### Frequency counting
```py3
from collections import Counter
frequencyDict = Counter(toCalculate)
```
- #### Own implementation of frequency counting
```py3
def frequencyCounter(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
            
    return freq
```
### Graph Traversal

#### • Inorder (Left, Root, Right) Stack
```py3
```
#### • Preorder (Root, Left, Right) Stack
```py3
```
#### • Postorder (Left, Right, Root) Stack
```py3
```
#### • Levelorder (BFS) Queue
```py3
```
#### • DFS (Recursion)
```py3
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
#### Dijkstra's Algorithm [LeetCode Minimum Cost Problem](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
```py3
```
#### Minimum Spanning Tree [LeetCode MST Problem](https://leetcode.com/problems/min-cost-to-connect-all-points/)
> prim's algorithm
```py3
```
