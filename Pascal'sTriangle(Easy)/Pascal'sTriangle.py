class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dummy = [[1]]
        for i in range(numRows - 1):
            temp = [0] + dummy[-1] + [0]
            row = []
            for j in range(len(dummy[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            dummy.append(row)
        return dummy