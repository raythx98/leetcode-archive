// time = O(n)
// space = O(1)

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 3) return n;
        int first = 1, second = 2, third = 3;
        for (int i = 3; i < n; i++) {
            first = second;
            second = third;
            third = first + second;
        }
        return third;
    }
};
