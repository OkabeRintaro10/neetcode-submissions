class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(letter.lower() for letter in s if letter.isalnum())
        is_palindrom = cleaned == cleaned[::-1]
        return is_palindrom