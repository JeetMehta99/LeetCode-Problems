class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words: # edge case
            return None
        
        freqWords = {}
        maxFreq = 1 # keeps track of freq of word for highest freq
        wordsList = []
        
        # checks frequency of words
        for word in words:
            if word not in freqWords:
                freqWords[word] = 1
            else:
                freqWords[word] += 1
                maxFreq = max(maxFreq, freqWords[word])
          
        # highest to lowest freq
        freq = maxFreq
        while freq >= 1:
            temp = [] # highest freq first appended
            for wor in freqWords:
                if freqWords[wor] == freq: # collecting highest to lowest freq words
                    temp.append(wor)
            temp = sorted(temp) # in case same freq then lexicographical order
            for ele in temp:
                wordsList.append(ele)
                if len(wordsList) == k:
                    return wordsList
            freq -= 1