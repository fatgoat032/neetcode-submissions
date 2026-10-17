class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_list = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = False
                    if j + 1 > len(nums2) - 1:
                        my_list.append(-1)
                    else:
                        for k in range(j + 1, len(nums2)):
                          if nums2[k] > nums2[j]:
                            found = True
                            my_list.append(nums2[k])
                            print(my_list)
                            break
                        if found == False:
                            my_list.append(-1)
        return my_list
        