class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prods = list()
        post_prods = list()
        self_prods = list()
        #find prefix prods
        prefix = 1
        postfix = 1
        for n in nums:
            prefix *= n
            pre_prods.append(prefix)
        
        for i in range(len(nums)-1, -1, -1):
            postfix *= nums[i]
            post_prods.append(postfix)
        post_prods.reverse()
    
        for i in range(len(nums)):
            if i == 0:
                self_prods.append(post_prods[i+1])
            elif i == len(nums) - 1:
                self_prods.append(pre_prods[i-1])
            else:
                self_prods.append(pre_prods[i-1] * post_prods[i+1])
        return self_prods
