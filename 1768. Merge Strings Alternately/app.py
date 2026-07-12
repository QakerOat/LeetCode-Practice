class Solution(object):
    def mergeAlternately(self, word1, word2):
        newWord = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                newWord += word1[i]
                newWord += word2[i]
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                newWord += word1[i]
                newWord += word2[i]
            newWord += word1[len(word2) - len(word1):]
        else:
            for i in range(len(word1)):
                newWord += word1[i]
                newWord += word2[i]
            newWord += word2[len(word1) - len(word2):]
        print(newWord)

Solution().mergeAlternately(word1 = "abcd", word2 = "pq")
