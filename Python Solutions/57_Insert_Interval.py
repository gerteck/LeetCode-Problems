from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        new_list = []

        if len(intervals) == 0:
            new_list.append(newInterval)
            return new_list

        given_start = newInterval[0]
        given_end = newInterval[1]
        minima = None
        maxima = None
        filled = False

        # [[1, 3], [6, 9]], newInterval = [2, 5]

        for interval in intervals:
            current_start = interval[0]
            current_end = interval[1]

            # Next iteration: waiting for maxima
            if minima is not None:
                # end is smaller than current
                if given_end < current_start:
                    new_list.append([minima, given_end])
                    minima = None
                    filled = True
                # inside current interval
                elif given_end <= current_end:
                    new_list.append([minima, current_end])
                    minima = None
                    filled = True
                    continue

            if not filled and minima is None:
                # If interval is before start:
                if current_end < given_start:
                    new_list.append(interval)
                    continue

            # if we have passed given interval
            if not filled and minima is None:
                if given_end < current_start:
                    new_list.append(newInterval)
                    filled = True

            if not filled and minima is None:
                # end lies in current interval, and no minima recorded:
                if current_start <= given_end <= current_end:
                    minima = min(current_start, given_start)
                    new_list.append([minima, current_end])
                    minima = None
                    filled = True
                    continue

            # start lies in current interval, not sure about end:
            if current_start <= given_start <= current_end:
                minima = current_start

                # If given end ends inside interval
                if given_end <= current_end:
                    new_list.append([minima, current_end])
                    filled = True
                    minima = None

            if filled:
                if current_start > given_end:
                    new_list.append(interval)

        # Not filled
        if not filled:
            if minima is not None:
                new_list.append([minima, given_end])
            if minima is None:
                new_list.append(newInterval)

        return new_list


# Question requires us to insert the new interval into the array,
# And if need be, merge intervals such that there will be no
# overlapping intervals in the end.

# To find start of new interval, we need to see if either:
#   start of new interval lies in any existing interval

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
a = Solution()

print(a.insert([[1,3],[6,9]], [2,5]))