// time = O(n)
// space = O(1)

// Moore's Voting Algorithm

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int poll, votes = 0;
        for (auto &num: nums) {
            if (!votes) {
                poll = num;
                votes = 1;
            } else if (num == poll) {
                votes++;
            } else {
                votes--;
            }
        }
        return poll;
    }
};