class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        Reverse = 0
        while(x > 0):
            Reminder = x %10
            Reverse = (Reverse *10) + Reminder
            x = x //10
        if (y==Reverse):
            return True
        else:
            return False
