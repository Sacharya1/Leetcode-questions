class Solution {
public:

    int findGCD(int A, int B){
        if(!B) return A;
        return findGCD(B, A%B);
    }

    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* result = head;
        while(head->next){
            
            ListNode* newNode = new ListNode(findGCD(head->val, head->next->val));
            ListNode* next = head->next;
            head->next = newNode;
            head->next->next = next;
            head = next;
        }

        return result;
        
    }
};
