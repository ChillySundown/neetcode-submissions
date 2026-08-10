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
    bool hasCycle(ListNode* head) {
        std::unordered_set<ListNode*> visited_nodes;
        ListNode* current {head};
        while(current != nullptr) {
            if(visited_nodes.contains(current)) {
                return true;
            } else {
                visited_nodes.insert(current);
                current = current->next;
            }
        }
        return false;
    }
};
