// time = O(n)
// space = O(1)

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fast = head;
        while (fast && fast->next) {
            fast = fast->next->next;
            head = head->next;
        }
        return head;
    }
};