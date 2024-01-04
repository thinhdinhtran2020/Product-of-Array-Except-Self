class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            new_nums = []
            
            res.append(prod(new_nums))
        return res
    
def main():
    solution = Solution()
    solution.productExceptSelf([1,2,3,4])
main()
