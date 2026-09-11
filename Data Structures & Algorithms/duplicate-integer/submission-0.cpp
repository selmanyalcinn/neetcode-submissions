#include <unordered_set>
#include <iostream>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> my_set; 
        for(int my_num : nums){
            if(my_set.contains(my_num)==true){
                return true;
            }else{
                my_set.insert(my_num);
            }
        }
        return false;
    }
};