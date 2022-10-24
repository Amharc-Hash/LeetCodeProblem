class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i in range(len(x)):
            if(x[i] != x[len(x)-i-1]):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(-121))
        