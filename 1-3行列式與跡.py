import numpy as np

# 1. 行列式：主要用於判定矩陣是否可逆。如果行列式為零，矩陣不可逆。
def is_invertible(matrix):
    """
    判定矩陣是否可逆：通過行列式判斷
    :param matrix: 方陣
    :return: 如果行列式不為0，則矩陣可逆，返回True；否則返回False
    """
    determinant = np.linalg.det(matrix)
    if determinant != 0:
        return True
    else:
        return False

# 2. 行列式在幾何學中的應用：描述線性變換是否會改變體積
def check_volume_change(matrix):
    """
    檢查線性變換是否改變體積：行列式的值可以告訴我們體積是否改變
    :param matrix: 方陣
    :return: 返回有關體積變化的信息。如果行列式為1，體積不變；如果不為1，體積改變。
    """
    determinant = np.linalg.det(matrix)
    if determinant == 1:
        return "體積不變"
    elif determinant == 0:
        return "體積壓縮到零（不可逆）"
    else:
        return f"體積被縮放了：{determinant}"

# 3. 行列式在物理學中的應用：檢查物理系統是否存在對稱性
def check_symmetry(matrix):
    """
    檢查矩陣是否具對稱性，這可以應用於物理學中的對稱性檢查
    :param matrix: 方陣
    :return: 返回矩陣是否對稱
    """
    return np.array_equal(matrix, matrix.T)  # 如果矩陣等於其轉置，則是對稱的

# 4. 跡：用於計算矩陣特徵值之和
def trace_vs_eigenvalues(matrix):
    """
    比較矩陣的跡與特徵值之和
    :param matrix: 方陣
    :return: 跡和特徵值的總和
    """
    trace_value = np.trace(matrix)  # 計算矩陣的跡（對角線元素之和）
    eigenvalues = np.linalg.eigvals(matrix)  # 計算矩陣的特徵值
    eigenvalue_sum = np.sum(eigenvalues)  # 特徵值的總和
    
    return trace_value, eigenvalue_sum

# 5. 跡在量子力學中的應用：確保密度矩陣的概率和為1
def check_density_matrix(matrix):
    """
    檢查密度矩陣的跡是否為1（量子力學中的應用，檢查概率和是否為1）
    :param matrix: 密度矩陣
    :return: True表示符合概率規範，False表示不符合
    """
    trace_value = np.trace(matrix)
    if np.isclose(trace_value, 1):  # 跡應為1表示概率和為1
        return True
    else:
        return False

# 6. 跡在線性代數中的應用：計算矩陣的算術平均值（對角元素的和）
def trace_arithmetic_mean(matrix):
    """
    計算矩陣對角線元素的平均值，這是一種統計性質，應用於線性代數
    :param matrix: 方陣
    :return: 矩陣對角線元素的平均值
    """
    trace_value = np.trace(matrix)
    return trace_value / len(matrix)  # 算術平均值是跡除以矩陣的階數


# 範例矩陣
matrix_2x2 = np.array([[4, 2], [3, 1]])
matrix_singular = np.array([[1, 2], [2, 4]])  # 行列式為0的奇異矩陣
matrix_3x3 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])  # 3x3矩陣
density_matrix = np.array([[0.5, 0.3], [0.3, 0.5]])  # 密度矩陣

# 應用 1: 檢查矩陣是否可逆
print(f"矩陣 {matrix_2x2} 可逆: {is_invertible(matrix_2x2)}")
print(f"矩陣 {matrix_singular} 可逆: {is_invertible(matrix_singular)}")

# 應用 2: 檢查線性變換是否改變體積
print(f"矩陣 {matrix_3x3} 的線性變換: {check_volume_change(matrix_3x3)}")

# 應用 3: 檢查物理系統的對稱性
print(f"矩陣 {matrix_3x3} 是否對稱: {check_symmetry(matrix_3x3)}")

# 應用 4: 比較矩陣的跡與特徵值之和
trace_value, eigenvalue_sum = trace_vs_eigenvalues(matrix_3x3)
print(f"矩陣的跡: {trace_value}, 特徵值之和: {eigenvalue_sum}")

# 應用 5: 檢查密度矩陣的概率規範
print(f"密度矩陣符合概率規範: {check_density_matrix(density_matrix)}")

# 應用 6: 計算矩陣的算術平均值
print(f"矩陣對角線元素的平均值: {trace_arithmetic_mean(matrix_3x3)}")

"""
應用總結：
行列式的應用：

用於判斷矩陣是否可逆：如果行列式為零，矩陣不可逆。
在幾何學中用於檢查線性變換是否改變體積：行列式為 1 表示體積不變，為 0 表示體積壓縮為零。
在物理學中可用於檢查矩陣的對稱性：對稱矩陣通常表示物理系統的某些對稱性。
跡的應用：

跡是矩陣特徵值的總和，因此可以用來進行特徵值分析。
在量子力學中，跡用於檢查密度矩陣的概率和是否為 1。
跡也可以用來計算矩陣的算術平均值，這是線性代數中的統計應用。

"""