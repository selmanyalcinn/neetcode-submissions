#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
       unordered_map <char,int> c1;
       unordered_map <char,int> c2;

        if(s.length()!=t.length()){
            return false;
        }

       for(char c:s){
        if(c1.contains(c)){
            c1[c]++;
        }else{
            c1[c]=1;
        }
       } 

       for(char c:t){
        if(c2.contains(c)){
            c2[c]++;
        }
        else{
            c2[c]=1;
        }
       }

       for(auto a:c1){
        char elem=a.first;
        int count=a.second;
        cout<<elem<<endl;
        if(!c2.contains(elem) || count!=c2[elem]){
            return false;
        }
       }

       return true;

    }
};
