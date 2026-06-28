#include <unordered_set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> my_set;
        for(int i:nums){
            if(my_set.count(i)){
                return true;
            }else{
                my_set.insert(i);
            }
        }
        return false;
    }
};