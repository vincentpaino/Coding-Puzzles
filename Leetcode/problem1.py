# Navigate to miniconda environment: conda activate Coding-Puzzles

import math

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary of key/value pairs of roman numeral strings/values.
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(s)):
            char = s[i]
            if roman_map[char]:
                






if __name__ == "__main__":
    result = Solution.romanToInt(self, "IV")
    print(f"The solution is: {result}")