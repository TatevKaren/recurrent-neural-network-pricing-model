import torch

# Create a 3x3 tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Indexing: Accessing a specific element
element = tensor[1, 2]  # Accessing element at row 1, column 2 (0-indexed)
print(f'Element at (1, 2): {element.item()}\n')

# Slicing: Accessing a subset of the tensor
subset = tensor[1:, 1:]  # Accessing all rows from 1 onwards, and all columns from 1 onwards
print(f'Subset:\n{subset}\n')

# Modifying a specific element
tensor[0, 0] = 10
print(f'Modified Tensor:\n{tensor}\n')

# Modifying a subset of the tensor
tensor[:, :2] = 0  # Setting all elements in the first and second columns to 0
print(f'Modified Tensor:\n{tensor}\n')

# Advanced Indexing: Accessing non-contiguous indices
rows = torch.tensor([0, 2])
cols = torch.tensor([1, 2])
selected = tensor[rows, cols]  # Accessing elements at (0, 1) and (2, 2)
print(f'Selected Elements: {selected}\n')
