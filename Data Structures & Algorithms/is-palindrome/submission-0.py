class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for c in s:
            if c.isalnum():
                palindrome = c.lower() + palindrome
        print(palindrome)
        return palindrome == palindrome[::-1]