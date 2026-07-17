class Solution {
public:
    bool isValid(string s) {
        vector<char> str_stack;
        unordered_map<char, int> closers{
            {']', 0},
            {')',1},
            {'}', 2}
        };
        unordered_map<char, char> complements{
            {'[', ']'},
            {'(', ')'},
            {'{', '}'}
        };
        for(int i = 0; i < s.size(); i++) {
            if(!str_stack.empty() && closers.contains(s[i])) {
                char match = complements[str_stack.back()];
                if(match != s[i]) {
                    return false;
                }
                else {
                    str_stack.pop_back();
                }
            } else {
                str_stack.push_back(s[i]);
            }
        }
        return str_stack.empty();
    }
};
