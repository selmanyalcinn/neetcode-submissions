class Solution {
public:
    bool isPalindrome(string s) {
        string my_string="";
        for(char c:s){
            if(isalnum(c)){
                my_string=my_string+(char)tolower(c);
            }
        }

        for(int i=0;i<my_string.size();i++){
            if(my_string[i]!=my_string[my_string.size()-1-i]){
                return false;
            }
        }

        return true;

    }
};
