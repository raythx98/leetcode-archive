# time: O(n)
# space: O(n)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        last_letter_occurence = {}
        words = s.split()
        words_set = set()
        if len(words) != len(pattern): return False
        for idx, (word, letter) in enumerate(zip(words, pattern)):
            if letter not in last_letter_occurence:
                if word in words_set:
                    return False
                words_set.add(word)
                last_letter_occurence[letter] = idx
                continue

            last_idx = last_letter_occurence[letter]
            if words[last_idx] != word:
                return False
        return True