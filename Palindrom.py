class Palindrom:

    def find_longest_palindrome(self,word:str) -> str:
        long = len(word)
        longest_palindrome = ""
        
        for i in range(long):
            for j in range(i, long):
                substring = word[i:j+1]
                if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
        if len(longest_palindrome) == 1:
            return ""
        return longest_palindrome
obj = Palindrom()
print(obj.find_longest_palindrome("abaab"))
