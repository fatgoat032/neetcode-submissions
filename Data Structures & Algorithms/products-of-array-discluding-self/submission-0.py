class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products_left = [1 for i in range(len(nums))]
        products_right = [1 for i in range(len(nums))]
        output_for_all = [1 for i in range(len(nums))]
        product_so_far = 1
        for i in range(len(nums) - 1):
            product_so_far *= nums[i]
            products_left[i + 1] = product_so_far
        product_so_far = 1
        for i in reversed(range(len(nums) - 1)):
            product_so_far *= nums[i + 1]
            products_right[i] = product_so_far
        for i in range(len(nums)):
            output_for_all[i] = products_left[i] * products_right[i]
        return output_for_all