'''
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in 
Reverse Polish Notation.

Evaluate the expression and return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in reverse Polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: 
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''



class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        last = 0
        ops = ('+','-','/','*')
        while tokens:
            cur = tokens.pop(0)
            if cur in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                n = 30
                if cur == '*':
                    n = num1 * num2
                elif cur == '/':
                    n = int(float(num1) / float(num2))
                elif cur == '+':
                    n = num1 + num2
                elif cur == '-':   
                    n = num1 - num2
                stack.append(n)
                last = n
                print('last: ',last)
            else:
                stack.append(int(cur))
                last = int(cur)
        return last