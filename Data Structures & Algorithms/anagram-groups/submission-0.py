from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        for s in strs:
            sortedkey="".join(sorted(s))
            anagram[sortedkey].append(s)
        return list(anagram.values())


        