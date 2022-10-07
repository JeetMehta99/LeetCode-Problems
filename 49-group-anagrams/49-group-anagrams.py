class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordList = []
        
        for word in strs:
            wordList.append(sorted(word))
            
        # print(wordList)
        letter = []
        for letter_list in wordList:
            letter.append(''.join(letter_list))

        wordSet = dict()
        for idx,val in enumerate(letter):
            if val in wordSet:
                wordSet[val].append(strs[idx])
            else:
                wordSet[val] = [strs[idx]]
        return [wordSet[x] for x in wordSet]