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
void recursiveHelper(ListNode*& prev, ListNode*& curr, int n, int& count) {
        if(curr) {
            recursiveHelper(curr, curr->next, n, count);
            count++;
        }
        
        if(count == n) {
            if(curr && prev) {
                prev->next = curr->next;
            } else if(prev) {
                prev->next = curr;
            } else {
                curr = curr->next;
            }
        }   
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int count = 0;
        ListNode* prev = nullptr;
        ListNode*& h = head;
        recursiveHelper(prev, h, n, count);
        return head;
    }
};
