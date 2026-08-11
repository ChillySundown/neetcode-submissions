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
    void reorderList(ListNode* head) {
        //Split List
        ListNode* i = head;
        ListNode* j = head->next;
        while(j != nullptr && j->next != nullptr) {
            i = i->next;
            j = j->next->next;
        }
        ListNode* second_half = i->next;
        //Reverse other half
        ListNode* prev = nullptr;
        i->next = nullptr;
        while(second_half != nullptr) {
            ListNode* temp = second_half->next;
            second_half->next = prev;
            prev = second_half;
            second_half = temp;
        }

        //Merge Lists
        while(prev != nullptr) {
            ListNode* temp1 = head->next;
            ListNode* temp2 = prev->next;

            head->next = prev;
            prev->next = temp1;

            head = temp1;
            prev = temp2;
        }

    }
};
