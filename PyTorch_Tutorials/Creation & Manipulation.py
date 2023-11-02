import torch
import numpy as np

# Create a NumPy array
numpy_array = np.array([[1, 2], [3, 4]])

# Convert the NumPy array to a PyTorch tensor
tensor_from_numpy = torch.tensor(numpy_array)
print(tensor_from_numpy)

# Create a tensor directly with specific values
tensor = torch.tensor([[1, 2], [3, 4]])

print(tensor)

# Create a tensor of zeros with specified size
zero_tensor = torch.zeros((2, 2))
print(zero_tensor)

# Create a tensor of ones with specified size
ones_tensor = torch.ones((2, 2))
print(ones_tensor)

# Create a random tensor with specified size
random_tensor = torch.rand((2, 2))
print(random_tensor)

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Add a scalar value to all elements of the tensor
added_scalar_tensor = tensor + 2
print(added_scalar_tensor)

# Multiply tensor elements
multiplied_tensor = tensor * tensor

print(multiplied_tensor)
# Reshape the tensor
reshaped_tensor = tensor.view(1, 4)
print(reshaped_tensor)

# Transpose the tensor
transposed_tensor = tensor.t()
print(transposed_tensor)

