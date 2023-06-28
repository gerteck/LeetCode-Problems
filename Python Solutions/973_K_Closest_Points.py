from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # def compare(p1, p2):
        #     p1_dist = (p1[0] + p1[1] )^0.5
        #     p2_dist = (p2[0] + p2[1] )^0.5
        #     return p1_dist - p2_dist

        def compare_key(p):
            return pow((p[0]**2 + p[1]**2), 0.5)

        points.sort(key=compare_key)
        # print(points)
        # sorted(points, key=compare)
        new_list = []

        for i in range(k):
            new_list.append(points[i])

        return new_list


a = Solution()
print(a.kClosest([[3,3],[5,-1],[-2,4]], 2))