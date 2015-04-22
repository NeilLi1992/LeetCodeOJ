# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "<" + str(self.x) +"," + str(self.y) + ">"

    def __str__(self):
        return "<" + str(self.x) +"," + str(self.y) + ">"

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)


        point_count = {}
        unique_points = []
        for point in points:
            if (point.x, point.y) in point_count:
                point_count[(point.x, point.y)] += 1
            else:
                point_count[(point.x, point.y)] = 1
                unique_points.append(point)

        if len(unique_points) == 1:
            return len(points)

        line_set = {}
        for i in range(len(unique_points)):
            for j in range(i+1, len(unique_points)):
                p1 = unique_points[i]
                p2 = unique_points[j]

                if p1.x == p2.x:
                    # x = b
                    k = None
                    b = p1.x
                else:
                    # y = kx + b
                    k = float(p1.y - p2.y) / (p1.x - p2.x)
                    b = p1.y - k * p1.x

                if (k, b) in line_set:
                    line_set[(k, b)].add(p1)
                    line_set[(k, b)].add(p2)
                else:
                    line_set[(k, b)] = set([p1, p2])

        max_count = -float("inf")
        for line, point_set in line_set.iteritems():
            local_count = 0
            for point in point_set:
                local_count += point_count[(point.x, point.y)]

            if local_count > max_count:
                max_count = local_count

        return max_count


points = [
    Point(1,1), Point(1,1), Point(1,1)
]

print Solution().maxPoints(points)
