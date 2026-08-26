from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            res[key].append(s)
        return(list(res.values()))


        
        