/* 
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:

* 1 <= a.length, b.length <= 104
* a and b consist only of '0' or '1' characters.
* Each string does not contain leading zeros except for the zero itself.
*/

class Solution{
        public int toInt(String s){
            int num = 0;
            int strLen = s.length();
            int counter = 0;
            int added;
            for(int i = strLen - 1; i != 0; i--){
                if(s[i] == 1){
                    
                }
                counter++; // this variable is used for the exponentiated of 2^X --> 2^counter
            }
        }

        public string toString(int val){

        }
        public String addBinary(String a, String b) {
            String result = "";

    }
}

public class main{
    public static void main(String[] args) {
        String String1 = "101"
        String String2 = "10101"

        System.out.println(addBinary(String1, String2));
    }
}