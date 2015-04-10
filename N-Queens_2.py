# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution:
    # @return a list of lists of string
    def totalNQueens(self, n):
        self.solutions_count = 0
        self.n = n
        self.col_taken = [False for _ in range(n)]
        self.row_taken = [False for _ in range(n)]
        self.dia1_taken = [False for _ in range(2*n-1)]  # Main diagnol
        self.dia2_taken = [False for _ in range(2*n-1)]  # Sub diagnol

        self.search(0, [])

        return self.solutions_count

    def is_placable(self, row, col):
        if self.row_taken[row]:
            return False

        if self.col_taken[col]:
            return False

        # Calculate diagnol
        dia1 = row - col + self.n - 1
        if self.dia1_taken[dia1]:
            return False

        dia2 = row + col
        if self.dia2_taken[dia2]:
            return False

        return True

    def search(self, row, positions):
        for col in range(self.n):
            if self.is_placable(row, col):
                # Place at (row, col)
                if row == self.n - 1:
                    self.solutions_count += 1
                else:
                    # Mark this position
                    self.row_taken[row] = True
                    self.col_taken[col] = True
                    self.dia1_taken[row - col + self.n - 1] = True
                    self.dia2_taken[row + col] = True
                    positions.append(col)

                    # Search next row
                    self.search(row+1, positions)

                    # Clear this position
                    self.row_taken[row] = False
                    self.col_taken[col] = False
                    self.dia1_taken[row - col + self.n - 1] = False
                    self.dia2_taken[row + col] = False
                    positions.pop()
            else:
                continue
        else:
            return

print Solution().totalNQueens(4)
