class Solution(object):
    def solution(self, needle, haystack):
        index = 0
        start_index = -1
        last_index = len(needle) - 1
        occurrence = False

        for index in range(len(haystack)):
            saved_index = index
            if needle[0] == haystack[index]:
                start_index = index
                for j in range(0, len(needle)):
                    if needle[j] == haystack[index]:
                        occurrence = True
                        index += 1
                    else:
                        occurrence = False
            if occurrence == True:
                return start_index
            start_index = -1
            index = saved_index

        return start_index


if __name__ == "__main__":
    print(Solution().solution("pi", "pinnpi"))


