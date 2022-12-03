// time = O(n)
// space = O(n)

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        string word = strs.front();
        bool is_prefix = true;
        for (int i = 0; i < word.size() && is_prefix; i++) {
            for (int j = 1; j < strs.size(); j++) {
                if (strs[j][i] != word[i]) is_prefix = false;
            }
            if (is_prefix) prefix += word[i];
        }
        return prefix;
    }
};