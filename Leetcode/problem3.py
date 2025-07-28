class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 1:
            return prefix
        
        for i in range(1, len(strs)):
            newPrefix = ""
            string1 = strs[0]
            stringIndexed = strs[i]
            shorter_string = string1
            if len(string1) > len(stringIndexed):
                shorter_string = stringIndexed
            for j in range(0, len(shorter_string)):
                if string1[j] == stringIndexed[j]:
                    newPrefix += string1[j]
                    prefix = newPrefix
        return prefix

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["crate", "cram", "crawls"]))