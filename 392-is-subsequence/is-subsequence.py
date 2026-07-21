class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        i=0
        count=0
        ans=False
        for j in range(len(t)):
            if s[i]==t[j]:
                count+=1
                i+=1
                if count==len(s):
                    ans=True
                    break
        return ans
        
            

        