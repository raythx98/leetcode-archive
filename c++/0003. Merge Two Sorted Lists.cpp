// time = O(n)
// space = O(1)

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // ensure list1 contains smallest node
        if (!list1) return list2;
        if (!list2) return list1;
        if (list1->val > list2->val) {
            ListNode* temp = list1;
            list1 = list2;
            list2 = temp;
        }
        
        ListNode* head = list1;
        ListNode* prev = NULL;
        
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                prev = list1;
                list1 = list1->next;
            } else {
                ListNode* next_smallest = list2;
                list2 = list2->next;
                
                prev->next = next_smallest;
                next_smallest->next = list1;
                prev = prev->next;
            }
        }

        if (list2) prev->next = list2;
        return head;
    }
};