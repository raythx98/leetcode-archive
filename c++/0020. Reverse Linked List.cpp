// time = O(n)
// space = O(1)

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) return head;
        ListNode* temp;
        ListNode* curr = head;
        while (curr->next) {
            temp = curr->next;
            curr->next = curr->next->next;
            temp->next = head;
            head = temp;
        }
        return head;
    }
};