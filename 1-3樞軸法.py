import numpy as np

def gaussian_elimination_with_pivot(matrix):
    """
    使用部分樞軸選擇的高斯消去法來將矩陣簡化為上三角矩陣
    :param matrix: 方陣
    :return: 簡化為上三角矩陣的結果
    """
    mat = np.array(matrix, dtype=float)
    rows, cols = mat.shape
    
    for i in range(min(rows, cols)):
        # 部分樞軸選擇：選取當前列中絕對值最大的元素作為主元
        max_row = np.argmax(np.abs(mat[i:, i])) + i
        if mat[max_row, i] == 0:
            raise ValueError("矩陣是奇異矩陣，無法進行高斯消去")
        
        # 如果主元不是當前行，進行行交換
        if max_row != i:
            mat[[i, max_row]] = mat[[max_row, i]]
        
        # 將主元歸一化
        mat[i] = mat[i] / mat[i, i]
        
        # 使用主元消去以下所有行的元素
        for j in range(i + 1, rows):
            mat[j] = mat[j] - mat[i] * mat[j, i]
    
    return mat

# 範例矩陣
matrix = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
reduced_matrix = gaussian_elimination_with_pivot(matrix)

# 輸出降階後的矩陣
print("上三角矩陣：")
print(reduced_matrix)

"""
樞軸法的應用：
解線性方程組：樞軸法確保了高斯消去過程中的數值穩定性，避免浮點數運算中的精度問題。
LU 分解：在 LU 分解中，樞軸法能夠避免零主元的問題，從而提高分解的可靠性。
總結：
基元降階法 與 樞軸法 是密切相關的，兩者都涉及矩陣簡化，但樞軸法更強調選擇主元來進行穩定的數值運算。
在進行矩陣分解和解線性方程組時，樞軸法可以提高精度和穩定性，因此它在高斯消去法和 LU 分解等算法中被廣泛使用。

"""
