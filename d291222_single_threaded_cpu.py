# time: O()
# space: O()
from heapq import heappush, heappop
from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort(reverse=True, key=lambda x:x[0])
        timestamp = 0; order = []; min_heap = []
        for i in range(n):
            # if min_heap is empty and next task starts after completion
            # of current process, we can update timestamp to latest
            if not min_heap and tasks[-1][0] > timestamp:
                timestamp = tasks[-1][0]
            # add all with current timestamp into min_heap
            while tasks and tasks[-1][0] <= timestamp:
                heappush(min_heap, tasks.pop()[1:]) 
            # process next
            process_time, idx = heappop(min_heap)
            order.append(idx)
            timestamp += process_time
        return order
