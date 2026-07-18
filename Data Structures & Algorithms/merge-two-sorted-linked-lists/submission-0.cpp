/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* newHead = new ListNode(0, nullptr);
        ListNode* w = newHead;
        ListNode* i = list1;
        ListNode* j = list2;
        while(i != nullptr && j != nullptr) {
            if(i->val <= j->val) {
                w->next = i;
                i = i->next;
                w = w->next;
            } else {
                w->next = j;
                j = j->next;
                w = w->next;
            }
        }

        if(i == nullptr) {
            while(j != nullptr) {
                w->next = j;
                j = j->next;
                w = w->next;
            }
        } else {
            while(i != nullptr) {
                w->next = i;
                i = i->next;
                w = w->next;
            }
        }
        w = nullptr;
        newHead = newHead->next;
        return newHead;
        
    }
};
