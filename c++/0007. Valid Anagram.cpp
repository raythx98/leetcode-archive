// time = O(n)
// space = O(n)

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> freq;
        for (auto &c: s) {
            freq[c]++;
        }
        for (auto &c: t) {
            freq[c]--;
        }
        for (auto &pair: freq) {
            if (pair.second != 0) return false;
        }
        return true;
    }
};