class Solution(object):
    def romanToInt(self, s):
        sumInt = 0
        romanToInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 150,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        strTochar = [x for x in s]
        print(strTochar)
        for i in range(len(strTochar)):
            pass

        return sumInt





if __name__ == '__main__':
    s = Solution()
    s.romanToInt("III")
    