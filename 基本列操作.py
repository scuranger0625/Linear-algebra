import numpy as np

def row_swap(matrix, row1, row2):
    """
    交換矩陣的兩行
    Args:
        matrix: 需要進行行操作的矩陣
        row1: 需要交換的第一行索引
        row2: 需要交換的第二行索引
    Returns:
        matrix: 行交換後的矩陣
    """
    # 將 row1 和 row2 進行行交換
    matrix[[row1, row2]] = matrix[[row2, row1]]
    return matrix

def row_multiply(matrix, row, multiplier):
    """
    將矩陣的某一行乘以一個非零數字
    Args:
        matrix: 需要進行行操作的矩陣
        row: 需要乘以常數的行索引
        multiplier: 用來乘以行的非零數字
    Returns:
        matrix: 行數乘後的矩陣
    """
    # 將第 row 行的每一個元素乘以 multiplier
    matrix[row] = matrix[row] * multiplier
    return matrix

def row_add(matrix, row1, row2, multiplier):
    """
    將 row2 的 multiplier 倍數加到 row1 上，這是行加法操作
    Args:
        matrix: 需要進行行操作的矩陣
        row1: 被加的行索引，最終結果保存在此行中
        row2: 被乘以 multiplier 並加到 row1 的行
        multiplier: 用來乘以 row2 的常數倍
    Returns:
        matrix: 行加減操作後的矩陣
    """
    # 將 row2 的 multiplier 倍加到 row1 上
    matrix[row1] = matrix[row1] + multiplier * matrix[row2]
    return matrix

# 測試矩陣操作的合併範例
if __name__ == "__main__":
    # 創建一個示例矩陣
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    print("初始矩陣 A:")
    print(A)

    # 1. 行交換：交換第一行和第三行
    A = row_swap(A, 0, 2)
    print("\n交換第一行和第三行後的矩陣 A:")
    print(A)

    # 2. 行數乘：將第二行乘以 0.5
    A = row_multiply(A, 1, 0.5)
    print("\n將第二行乘以 0.5 後的矩陣 A:")
    print(A)

    # 3. 行加減：將第三行的 2 倍加到第一行上
    A = row_add(A, 0, 2, 2)
    print("\n將第三行的 2 倍加到第一行後的矩陣 A:")
    print(A)
