# Navigate to miniconda environment: conda activate Coding-Puzzles

import math

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary of key/value pairs of roman numeral strings/values.
        if len(s) > 15 and len(s) < 1:
            return

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
            total = 0

            if len(s) > 1:
                return
            else:
                if char == "I":
                    total += roman_map[char]

                if char == "V":
                    total += roman_map[char]

                if char == "X":
                    total += roman_map[char]
                    #while(s[i+1] == "X"):

                if char == "L":
                    total += roman_map[char]

                if char == "C":
                    total += roman_map[char]

                if char == "D":
                    total += roman_map[char]

                if char == "M":
                    total += roman_map[char]
                return total


                






if __name__ == "__main__":
    solution = Solution()
    result = solution.romanToInt('V')
    print(f"The solution is: {result}")