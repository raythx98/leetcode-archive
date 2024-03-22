# time: O(n)
# space: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ptr, t_ptr = len(s) - 1, len(t) - 1
        s_bs = t_bs = 0
        while s_ptr >= 0 or t_ptr >= 0:
            while s_ptr >= 0 and (s[s_ptr] == '#' or s_bs):
                s_bs += 1 if s[s_ptr] == '#' else -1
                s_ptr -= 1
            while t_ptr >= 0 and (t[t_ptr] == '#' or t_bs):
                t_bs += 1 if t[t_ptr] == '#' else -1
                t_ptr -= 1
            if t_ptr < 0 or s_ptr < 0:
                return t_ptr == s_ptr == -1
            if s[s_ptr] != t[t_ptr]:
                return False
            s_ptr -= 1; t_ptr -= 1
        return True