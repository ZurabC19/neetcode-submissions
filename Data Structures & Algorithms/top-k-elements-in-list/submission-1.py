class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums)+1)]
        count = {}

        for n in nums:
            count[n] = count.get(n,0) + 1

        for n,count in count.items():
            freq[count].append(n)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
            if  len(res) == k:
                return res


