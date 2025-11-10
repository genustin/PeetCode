class Solution(object):
    # https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1] # [start:stop:step]

# the testing part
sol = Solution()
print(sol.reverseString("abcdefg"))
print(range(10)[0:6:2])
print(range(10)[::-1]) #negative step only support all elements