class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Берём первую строку как "эталон"
        prefix = strs[0]
        
        for s in strs[1:]:
            # Уменьшаем prefix пока он не является началом строки s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # обрезаем последний символ
                if not prefix:
                    return ""
        
        return prefix