// time = O(n)
// space = O(n)

class Solution {
public:
    string addBinary(string a, string b) {
        int a_curr = a.size(), b_curr = b.size(), carry = 0;
        string str;
        while (a_curr || b_curr || carry) {
            if (a_curr) {
                carry += a[--a_curr] - '0';
            }
            if (b_curr) {
                carry += b[--b_curr] - '0';
            }
            str = char(carry % 2 + '0') + str;
            carry = carry>>1;
        }
        return str;
    }
};