'''
135. Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second, and third child with 2, 1, and 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second, and third child with 1, 2, and 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:
n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4
'''

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        candies = [1]*length
        for i in range(length-1):
            if ratings[i]<ratings[i+1]:
                candies[i+1] = candies[i]+1
        for i in range(length-1):
            if ratings[length-1-i]<ratings[length-2-i] and candies[length-2-i]<=candies[length-1-i]:
                candies[length-2-i] = candies[length-1-i]+1
        return sum(candies)