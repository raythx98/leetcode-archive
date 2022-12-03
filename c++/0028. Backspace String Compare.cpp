// time = O(n)
// space = O(n)

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        int s_curr = 0, t_curr = 0;
        for (auto &c: s) {
            if (c == '#') {
                if (s_curr > 0) s_curr--;
            } else {
                s[s_curr++] = c;
            }
        }
        
        for (auto &c: t) {
            if (c == '#') {
                if (t_curr > 0) t_curr--;
            } else {
                t[t_curr++] = c;
            }
        }
        return s.substr(0, s_curr) == t.substr(0, t_curr);
    }
};