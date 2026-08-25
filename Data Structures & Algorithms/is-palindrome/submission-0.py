class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s="".join(char for char in s if char.isalnum())
        lower_s=clean_s.lower()
        pal_s=lower_s[::-1]
        if lower_s==pal_s:
            return True
        return False
        