import torch

# Create two matrices
matrix1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
matrix2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Matrix Multiplication
matmul_result = torch.matmul(matrix1, matrix2)
print(f'Matrix Multiplication Result:\n{matmul_result}\n')

# Alternatively, you can use the @ operator for matrix multiplication
matmul_result_operator = matrix1 @ matrix2
print(f'Matrix Multiplication Result (using @ operator):\n{matmul_result_operator}\n')

# Transpose of a Matrix
transpose_result = torch.t(matrix1)
# or use matrix1.t()
print(f'Transpose Result:\n{transpose_result}\n')

# Dot Product
# For dot product, we'll flatten the matrices to vectors first
vector1 = matrix1.view(-1)
vector2 = matrix2.view(-1)
dot_product_result = torch.dot(vector1, vector2)
print(f'Dot Product Result:\n{dot_product_result}\n')

