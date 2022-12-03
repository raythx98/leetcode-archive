// time = O(n)
// space = O(1)

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman_mapping = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int num = 0;
        for (int i = 0; i < s.size() - 1; i++) {
            if (roman_mapping[s[i]] < roman_mapping[s[i+1]]) num -= roman_mapping[s[i]];
            else num += roman_mapping[s[i]];
        }
        return num + roman_mapping[s.back()];
    }
};