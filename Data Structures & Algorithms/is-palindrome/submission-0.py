class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = (''.join(ch for ch in s if ch.isalnum())).lower()
        left = 0
        right = len(result)-1
        print(result)
        while left < right:
            if result[left] != result[right]:
                print(left, right)
                print(result[left], result[right])
                return False
            left += 1
            right -= 1
        return True

        