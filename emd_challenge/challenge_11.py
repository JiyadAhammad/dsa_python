"""
pascal triangle
"""


class Solution:
    def generateRow(self, row: int) -> list[int]:
        result = 1
        ansRow: list[int] = []
        ansRow.append(result)
        for col in range(1, row):
            result = result * (row - col)
            result = result // col
            ansRow.append(result)

        return ansRow

    def generate(self, numRows: int) -> list[list[int]]:
        ans: list[list[int]] = []

        for i in range(1, numRows + 1):
            result = self.generateRow(i)
            ans.append(result)

        return ans
