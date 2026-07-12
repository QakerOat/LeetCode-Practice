class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ])
        myVowels = []
        newWord = []
        for letter in s:
            if letter in vowels:
                myVowels.append(letter)

        for letter in s:
            if letter not in vowels:
                newWord.append(letter)
            else:
                newWord.append(myVowels.pop())

        return ''.join(newWord)