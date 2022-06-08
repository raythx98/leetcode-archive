// time = O(n)
// space = O(n)

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> char_count;
        for (auto &c: magazine) {
            char_count[c]++;
        }
        for (auto &c: ransomNote) {
            if (--char_count[c] < 0) return false;
        }
        return true;
    }
};