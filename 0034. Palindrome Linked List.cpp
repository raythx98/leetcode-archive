// time = O(n)
// space = O(1)

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* fast = head; ListNode* slow = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode* prev = slow;
        slow = slow->next;
        prev->next = nullptr;
        while(slow) {
            ListNode* temp = slow;
            slow = slow->next;
            temp->next = prev;
            prev = temp;
        }
        while (prev) {
            if (head->val != prev->val) return false;
            head = head->next;
            prev = prev->next;
        }
        return true;
    }
};