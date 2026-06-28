class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        stack=[]
        for i in range(9):
            for m in range(9):
                if board[i][m]!="." and board[i].count(board[i][m])>1:
                    return False
                m+=1
            i+=1

        print("Satırlar Tamam")

        for a in range(9):
            for b in range(9):
                stack.append(board[b][a])
                if board[b][a] != "." and stack.count(board[b][a])>1:
                    return False
                b+=1
            a+=1
            stack=[]

        print("Sütunlar Tamam")
        for box_row in range(0, 9, 3):  # 0, 3, 6
            for box_col in range(0, 9, 3):  # 0, 3, 6
                seen = set()
                for i in range(3):
                    for j in range(3):
                        cell_value = board[box_row + i][box_col + j]
                        if cell_value != ".":
                            if cell_value in seen:
                                return False
                            seen.add(cell_value)

        print("✅ 3x3 Alt Kutular Geçerli")

        
        return True
        