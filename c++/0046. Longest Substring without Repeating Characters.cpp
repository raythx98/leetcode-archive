// time = O(n)
// space = O(1)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> char_freq(255, -1);
        
        int curr = 0;
        int longest_substrong = 0;
        for (int i = 0; i < s.size(); i++) {
            if (char_freq[s[i]] < i - curr) {
                curr++;
                char_freq[s[i]] = i;
                if (curr > longest_substrong) longest_substrong = curr;
            } else {
                curr = i - char_freq[s[i]];
                char_freq[s[i]] = i;
            }
        }
        return longest_substrong;
    }
};