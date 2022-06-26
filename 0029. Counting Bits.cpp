// time = O(n)
// space = O(n)

class Solution {
public:
    vector<int> countBits(int n) { 
        vector<int> one_bits = {0}; 
        while (one_bits.size() < n + 1) {
            int iterate_size = one_bits.size();
            for (int i = 0; i < iterate_size; i++) {
                one_bits.push_back(one_bits[i]+1);
                if (one_bits.size() == n + 1) return one_bits;
            }
        }
        return one_bits;
    }
};