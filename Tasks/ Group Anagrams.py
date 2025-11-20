class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            sortedString = ''.join(sorted(list(s.lower())))
            if sortedString in groups:
                groups[sortedString].append(s)
            else:
                groups[sortedString] = [s]
        return list(groups.values())
        
