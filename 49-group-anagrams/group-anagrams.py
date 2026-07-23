class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res={}
        for s in strs:
            t="".join(sorted(s))
            res.setdefault(t,[]).append(s)
        return list(res.values())

        