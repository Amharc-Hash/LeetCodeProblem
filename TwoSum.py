class Solution(object):
    def twoSum(self, nums, target):
        self.lst = nums
        self.tempLst = []
        for i in range(len(self.lst)):
            for j in range(i+1,len(self.lst)):
                if(self.lst[i] + self.lst[j] == target):
                    return [i,j]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    # print(s.twoSum([3,3], 6))
    # print(s.twoSum([3,2,4], 6))