#  Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# click to show follow up.
# Follow up:
#
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), donot return anything, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return

        row_to_remove = []
        col_to_remove = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    row_to_remove.append(i)
                    col_to_remove.append(j)

        for i in row_to_remove:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for j in col_to_remove:
            for i in range(len(matrix)):
                matrix[i][j] = 0
    
