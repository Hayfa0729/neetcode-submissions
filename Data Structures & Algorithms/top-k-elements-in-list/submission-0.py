class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = float('-inf')
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                hash_dict[nums[i]] += 1
            else:
                hash_dict[nums[i]] = 1
        max_key = 0
    
        result = []
        while k > 0:
            for value in hash_dict:
                if hash_dict[value] > max_freq:
                    max_freq = hash_dict[value]
                    max_key = value
            result.append(max_key)
            del hash_dict[max_key]
            max_freq = float('-inf')
            k -= 1 
        return result


        
        