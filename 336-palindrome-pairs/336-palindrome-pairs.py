# class Solution: 
#     # SUPER DIFFICULT. TIMOTHY SOLUTION ON YT. REVISIT AND REVISE AGAIN. 
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         # Brute Force would be O(n^2 * k). Prolly a TLE
#         n = len(words)
#         res = []
#         # helper func to check palindrome
#         def isPalindrome(word, start, end):
#             while start < end:
#                 if word[start] != word[end]: # begin is not equal to end and continue
#                     return False
#                 start += 1
#                 end -= 1
#             return True
        
#         lookup = {word: i for i, word in enumerate(words)} # hash. word:key, idx:val
#         for i in range(n):
#             word = words[i]
#             if word=="": # blank string
#                 for j in range(n):
#                     if i!= j and isPalindrome(words[j], 0, len(words[j])-1):
#                         res.append([i, j])
#                         res.append([j, i])
#                 continue
#             reverseWord = word[::-1]
#             if reverseWord in lookup and lookup[reverseWord] != i:
#                 res.append([i, lookup[reverseWord]])
#             for k in range(1, len(word)):
#                 if isPalindrome(word, 0, k-1) and word[k:][::-1] in lookup:
#                     res.append([lookup[word[k:][::-1]], i])
#                 if isPalindrome(word, k, len(word)-1) and word[:k][::-1] in lookup:
#                     res.append([i, lookup[word[:k][::-1]]])
#         return res
class Solution:
    def palindromePairs(self, words):

        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes

        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i + 1:])
            return valid_suffixes

        word_lookup = {word: i for i, word in enumerate(words)}
        solutions = []

        for word_index, word in enumerate(words):
            reversed_word = word[::-1]

            # Build solutions of case #1. This word will be word 1.
            if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
                solutions.append([word_index, word_lookup[reversed_word]])

            # Build solutions of case #2. This word will be word 2.
            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    solutions.append([word_lookup[reversed_suffix], word_index])

            # Build solutions of case #3. This word will be word 1.
            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    solutions.append([word_index, word_lookup[reversed_prefix]])

        return solutions