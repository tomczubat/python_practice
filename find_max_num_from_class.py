
class MaxNumberFinder:
    def __init__(self, nums):
        self.nums = nums
 
    def find_max_number(self):
        if not self.nums:
            return None
 
        return max(self.nums)
    
ob1 = MaxNumberFinder([1,2,3,4,50,505,606,7777,14,15])

print(ob1.find_max_number())