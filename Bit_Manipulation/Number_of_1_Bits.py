'''
191. Number of 1 Bits

Given a positive integer n, write a function that returns the number of set bits 
in its binary representation (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3

Binary Representation:
    11  ->  1011
Explanation: The binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1

Binary Representation:
   128  ->  10000000
Explanation: The binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30

Binary Representation:
  2147483645  ->  1111111111111111111111111111101
Explanation: The binary string has a total of thirty set bits.

Constraints:
- 1 <= n <= 2^31 - 1
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n>0:
            test = n % 2
            n = n//2
            if test:
                count += 1
        return count