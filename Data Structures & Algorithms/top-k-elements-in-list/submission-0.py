class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent = {} #hashmap
        the_list = []
        for i in range(len(nums)):
            most_frequent[str(nums[i])] = most_frequent.get(str(nums[i]), 0) + 1
        most_frequent_sorted = dict(sorted(most_frequent.items(), key=lambda item: item[1], reverse=True))
        for key in list(most_frequent_sorted)[:k]:
            the_list.append(key)
        return the_list
