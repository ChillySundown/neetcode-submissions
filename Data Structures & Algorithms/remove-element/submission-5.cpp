class Solution {
public:
    void shift_left(vector<int>& nums, int index) {
        for(int i = index; i < nums.size()-1; i++) {
            nums[i] = nums[i+1];
        }
    }
    void print_vector(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++) {
            std::cout << nums[i] << " ";
        }
    }

    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        int size = nums.size();
        for(int i = 0; i < size; i++) {
            print_vector(nums);
            std::cout << std::endl;
            if(nums[i] == val) {
                size--;
                shift_left(nums, i);
                i--;
            } else {
                k++;
            }
        }
        return k;
    }
};