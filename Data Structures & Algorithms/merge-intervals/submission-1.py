class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])

        res = [intervals[0]]
        for i in intervals:
            start = i[0]
            end = i[1]
            prev_end = res[-1][1]

            if prev_end >= start:
                res[-1][1]=max(prev_end,end)
            else:
                res.append([start,end])
        return res

        
        



# if prev_end >= start 
    