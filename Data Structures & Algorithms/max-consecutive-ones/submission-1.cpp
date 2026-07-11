class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_ones = 0;
        int current_ones = 0;
        for(int n : nums) {
            if(n == 1) {
                current_ones++;
                if(current_ones > max_ones) {
                    max_ones = current_ones;
                }
            } else {
                current_ones = 0;
            }
        }
        return max_ones;
    }
};