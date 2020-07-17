class Solution {
public:
    bool isPalindrome(int x) {
        long int digit,rev = 0;
        int y = x;
        
        if(x<0){
            return false;
        }
        do
        {
            digit = x % 10;
            rev = (rev * 10) + digit;
            x = x / 10;
        } while (x != 0);
        if(rev==y)return true;
        else return false;
        
    }
};
