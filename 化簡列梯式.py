import numpy as np

def rref(matrix):
    A = matrix.astype(float)  # 確保矩陣元素為浮點數，以進行除法
    rows, cols = A.shape
    col = 0  # 從第一列開始處理

    for row in range(rows):
        if col >= cols:
            break
        # 尋找當前列中最大元素的行，並進行行交換（以應對零主元）
        max_row = np.argmax(np.abs(A[row:, col])) + row
        if A[max_row, col] == 0:
            col += 1  # 如果當前列全為零，跳過該列
            continue
        # 行交換
        A[[row, max_row]] = A[[max_row, row]]
        
        # 將主元變為 1
        A[row] = A[row] / A[row, col]
        
        # 使用主元將其他行的該列元素消去
        for r in range(rows):
            if r != row:
                A[r] = A[r] - A[r, col] * A[row]
        
        # 移動到下一列
        col += 1

    return A

# 測試範例列梯式矩陣
A = np.array([[1, -1, -1, 0],
              [1, -1, -2, 3],
              [2, -1, -2, 1],
              [1, -2, -2, 2]])

# 使用函數轉換為化簡列梯式
rref_matrix = rref(A)

# 輸出結果
print(rref_matrix)
