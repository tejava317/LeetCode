class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        """
        direction
        0 : right
        1 : down
        2 : left
        3 : up
        """
        direction = 0
        boundary = [len(matrix[0]) - 1, len(matrix) - 1, 0, 1]
        i = 0
        j = 0
        
        while True:
            match direction:
                case 0:
                    ans.append(matrix[i][j])
                    if j < boundary[direction]:
                        j += 1
                    else:
                        boundary[direction] -= 1
                        direction = 1
                        i += 1
                        if (i > boundary[direction]):
                            break
                case 1:
                    ans.append(matrix[i][j])
                    if i < boundary[direction]:
                        i += 1
                    else:
                        boundary[direction] -= 1
                        direction = 2
                        j -= 1
                        if (j < boundary[direction]):
                            break
                case 2:
                    ans.append(matrix[i][j])
                    if j > boundary[direction]:
                        j -= 1
                    else:
                        boundary[direction] += 1
                        direction = 3
                        i -= 1
                        if (i < boundary[direction]):
                            break
                case 3:
                    ans.append(matrix[i][j])
                    if i > boundary[direction]:
                        i -= 1
                    else:
                        boundary[direction] += 1
                        direction = 0
                        j += 1
                        if (j > boundary[direction]):
                            break
                case _:
                    raise ValueError()

        return ans