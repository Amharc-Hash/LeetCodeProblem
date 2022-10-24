class Solution(object):
    def plusOne(self, digits):
        self.lst = []
        self.lst = digits
        self.strA = ""
        self.lst[-1] += 1

        self.lst.reverse()

        for i in range(len(self.lst)):
            if(self.lst[i] > 9):
                strA = [x for x in str(self.lst[i])]
                
                if(self.lst[-1] > 9):
                    self.lst[i] = int(strA[1])
                    self.lst.append(int(strA[0]))
                else:
                    self.lst[i] = int(strA[1])
                    self.lst[i+1] += int(strA[0])

        self.lst.reverse()
        return self.lst



if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9,9]))
    print(s.plusOne([1,2,9]))
    print(s.plusOne([4,8,9,9]))
    print(s.plusOne([4,9,9,9]))

    # s.plusOne([1,2,3,9])