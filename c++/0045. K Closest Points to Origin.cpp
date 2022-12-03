// time = O(nlgk)
// space = 

using pi = pair<int, vector<int>>;

class Compare {
public:
    bool operator() (pi &pair1, pi &pair2) {
        return pair1.first < pair2.first;
    }
};

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pi, vector<pi>, Compare> pq;
        for (auto &point: points) {
            int x = point.front(), y = point.back();
            pq.push({x*x+y*y, point});
            if (pq.size() > k) pq.pop();
        }
        
        points.clear();
        for (int i = 0; i< k; i++) {
            points.push_back(pq.top().second);
            pq.pop();
        }
        return points;
    }
};