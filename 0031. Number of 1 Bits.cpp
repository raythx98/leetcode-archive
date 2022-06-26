// time = O(n)
// space = O(1)

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int num_ones = 0;
        while (n > 0) {
            num_ones += n&1;
            n = n>>1;
        }
        return num_ones;
    }
};