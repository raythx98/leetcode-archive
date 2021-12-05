# leetcode-solutions

### Binary Search

#### • Minimum position with duplicates
```
int low = 0;
int high = size - 1;

// Loop invariant: index is between [low, high+1]

while (low <= high) {
    int mid = low + ((high-low)>>1);
    if (val[mid] < target) { // recurse right
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

// Loop invariant: index is between [low, high+1]

while (low <= high) {
    int mid = low + ((high-low)>>1);
    if (val[mid] < target) { // recurse right
        low = mid + 1;
    } else {
        high = mid - 1;
    }
}
```

### Sort

#### • Quick Sort (in-place, NOT stable)
```
```
#### • Merge Sort - Linked List (stable, NOT in-place)
```
```
#### • Merge Sort - Arrays (stable, NOT in-place)
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
