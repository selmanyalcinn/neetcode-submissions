#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int>my_map;
        unordered_map<char,int>my_map2;

        for(char c:s){
            if(!my_map.count(c)){
                my_map[c]=1;
            }else{
                my_map[c]++;
            }
        }
        for(char c:t){
            if(!my_map2.count(c)){
                my_map2[c]=1;
            }else{
                my_map2[c]++;
            }
        }
        if(my_map==my_map2){
            return true;
        }else{
            return false;
        }
    }
};
