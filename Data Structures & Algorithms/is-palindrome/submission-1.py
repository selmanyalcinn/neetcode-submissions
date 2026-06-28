class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Sadece harf ve rakamları al
        return s == s[::-1]  # Tersiyle aynı mı kontrol et
        