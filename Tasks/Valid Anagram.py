class Solution(object):
    def isAnagram(self, s, t):
        changed_s = sorted(list(s.lower()))
        changed_t = sorted(list(t.lower()))
        if changed_s == changed_t:
            return True
        return False
