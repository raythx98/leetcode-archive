// time = O(n)
// space = O(n)

class Solution {
public:
    bool isValid(string s) {
        stack<char> bracket_stack;
        for (auto &c : s) {
            if (c == '(' || c == '[' || c == '{') bracket_stack.push(c);
            else {
                if (bracket_stack.empty()) return false;
                if (c == ')') {
                    if (bracket_stack.top() != '(') return false;
                } else if (c == ']') {
                    if (bracket_stack.top() != '[') return false;
                } else if (c == '}') {
                    if (bracket_stack.top() != '{') return false;
                }
                bracket_stack.pop();   
            }
        }
        return bracket_stack.empty();
    }
};