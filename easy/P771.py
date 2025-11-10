class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        jewel_set = set(J)  # 使用集合来存储宝石字符，提高查找效率
        for stone in S:
            if stone in jewel_set:
                count += 1
        return count

J = "Asc"
S = "AAaaBBbbCCccDDdd"
sol = Solution()
print(sol.numJewelsInStones(J, S))