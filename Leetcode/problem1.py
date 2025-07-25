# Navigate to miniconda environment: conda activate Coding-Puzzles

import math

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary of key/value pairs of roman numeral strings/values.
        if s.length > 15 and s.length < 1:
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
                if roman_map[char] == "I":
                    total+=1

                if roman_map[char] == "V":
                    total+=5

                if roman_map[char] == "X":
                    total+=10
                    #while(s[i+1] == "X"):

                if roman_map[char] == "L":
                    total+=50

                if roman_map[char] == "C":
                    total+=100

                if roman_map[char] == "D":
                    total+=500

                if roman_map[char] == "M":
                    total+=1000
                return total


                






if __name__ == "__main__":
    result = Solution.romanToInt(self, "IV")
    print(f"The solution is: {result}")